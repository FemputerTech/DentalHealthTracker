from flask import Blueprint, render_template
from flask_login import current_user, login_required


dash = Blueprint("dash", __name__)

@dash.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)