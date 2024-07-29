from flask import Blueprint, render_template, jsonify
from flask_login import current_user, login_required, logout_user
from .models import User


views = Blueprint("views", __name__)


@views.route("/", methods=["GET"])
def index():
    print({"details":"It's aliiiiive!!"})
    logout_user()
    return render_template("index.html", user=current_user)


@views.route("/about", methods=["GET"])
def about():
    return render_template("about.html", user=current_user)


@views.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)


@views.route("/popup/<popup>", methods=["GET"])
@login_required
def load_popup(popup):
    return render_template(f"partials/{popup}.html", user=current_user)


@views.route("/account", methods=["GET"])
@login_required
def account():
    user_id = current_user.id
    user = User.query.filter_by(id=user_id).first()
    user_data = [{
        "account_number": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "dob": user.dob,
        "tel": user.tel,
        "dentist": user.dentist_id
    }] 
    return jsonify({"user": user_data})