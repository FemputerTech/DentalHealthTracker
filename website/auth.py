from flask import Blueprint, render_template, redirect, url_for
from website.forms import SignupForm, LoginForm
from .extensions import db, bcrypt
from .models import User


auth = Blueprint("auth", __name__)


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            dob = form.dob.data,
            tel = form.tel.data,
            password = hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    else:
        print(form.errors)
    return render_template('signup.html', form=form)


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)