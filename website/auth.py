from flask import Blueprint, request, render_template, redirect, url_for
from email_validator import validate_email, EmailNotValidError
from phonenumbers import parse, NumberParseException, is_valid_number
from flask_login import login_user, login_required, logout_user, current_user
from datetime import datetime
from .extensions import db, bcrypt
from .models import User


auth = Blueprint("auth", __name__)


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        errors = {}
        first_name = request.form.get("first-name")
        last_name = request.form.get("last-name")
        email = request.form.get("email")
        dob = request.form.get("dob")
        tel = request.form.get("tel")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm-password")

        # Validate inputs
        if not (1 <= len(first_name) <= 40):
            errors["first_name"] = "First name must be between 1 and 40 characters."

        if not (1 <= len(last_name) <= 80):
            errors["last_name"] = "Last name must be between 1 and 80 characters."

        try:
            validate_email(email)
        except EmailNotValidError:
            errors["email"] = "Invalid email address."

        # Check if user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            errors["email"] = "That email already exists. Please choose a different one."
        
        try:
            datetime.strptime(dob, "%Y-%m-%d")
        except ValueError:
            errors["dob"] = "Invalid date of birth format. Use YYYY-MM-DD."

        # try:
        #     phone_number = parse(tel)
        #     if not is_valid_number(phone_number):
        #         errors.append({"Tel Error":"Invalid phone number."})
        # except NumberParseException:
        #     errors.append({"Tel Error":"Invalid phone format."})

        if not (8 <= len(password) <= 20):
            errors["password"] = "Password must be between 8 and 20 characters."

        if confirm_password != password:
            errors["confirm_password"] = "Passwords must match."
            
        if errors:    
            return render_template('signup.html', user=current_user, errors=errors)

        # convert dob to date
        dob = datetime.strptime(dob, "%Y-%m-%d").date()

        hashed_password = bcrypt.generate_password_hash(password)
        new_user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            dob = dob,
            tel = tel,
            password = hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login'))

    return render_template('signup.html', user=current_user, errors={})


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if bcrypt.check_password_hash(user.password, password):
                login_user(user, remember=True)
                return redirect(url_for("dash.dashboard"))
            else:
                print({"Password Login Error":"Incorrect password"})
        else:
            print({"Email Login Error":"Email does not exists"})

    return render_template('login.html', user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.index"))