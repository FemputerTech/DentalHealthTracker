from flask import Blueprint, render_template
from flask_login import current_user


views = Blueprint("views", __name__)


@views.route("/", methods=["GET"])
def index():
    print({"details":"It's aliiiiive!!"})
    return render_template("index.html", user=current_user)


@views.route("/about", methods=["GET"])
def about():
    return render_template("about.html", user=current_user)