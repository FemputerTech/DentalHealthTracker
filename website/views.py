from flask import Blueprint, render_template, jsonify
from flask_login import current_user, login_required, logout_user


views = Blueprint("views", __name__)


@views.route("/", methods=["GET"])
def index():
    print({"details":"It's aliiiiive!!"})
    logout_user()
    return render_template("index.html", user=current_user)


@views.route("/about", methods=["GET"])
def about():
    return render_template("about.html", user=current_user)


@views.route("/popup/<popup>", methods=["GET"])
@login_required
def load_popup(popup):
    return render_template(f"partials/{popup}.html", user=current_user)