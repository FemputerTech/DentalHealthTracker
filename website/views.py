from flask import Blueprint, render_template


views = Blueprint("views", __name__)


@views.route("/", methods=["GET"])
def index():
    print({"details":"It's aliiiiive!!"})
    return render_template("index.html")


@views.route("/about", methods=["GET"])
def about():
    return render_template("about.html")


@views.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    return render_template("dashboard.html")