from flask import Blueprint, render_template
from flask_login import current_user, login_required


views = Blueprint("views", __name__)


@views.route("/", methods=["GET"])
def index():
    print({"details":"It's aliiiiive!!"})
    return render_template("index.html", user=current_user)


@views.route("/about", methods=["GET"])
def about():
    return render_template("about.html", user=current_user)


@views.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)


@views.route("/dashboard/<section>", methods=["GET"])
@login_required
def load_content(section):
    return render_template(f"partials/{section}.html")


@views.route("/popup/<popup>", methods=["GET"])
@login_required
def load_popup(popup):
    return render_template(f"partials/{popup}.html", user=current_user)