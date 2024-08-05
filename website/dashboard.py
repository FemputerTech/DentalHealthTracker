from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from .models import Chat, Dentist
from .extensions import db


dash = Blueprint("dash", __name__)

@dash.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    user_id = current_user.id
    print("current primary dentist:", current_user.dentist_id)
    messages = Chat.query.filter_by(user_id=user_id).order_by(Chat.timestamp).all()
    dentists = Dentist.query.order_by(Dentist.id).all()
    formatted_messages = [{"role": message.role, "content": message.content} for message in messages]

    if request.method == "POST":
        new_dentist_id = request.form.get("dentist_id")
        print("dentist id: ", new_dentist_id)
        if new_dentist_id:
            current_user.dentist_id = new_dentist_id
            db.session.commit()
            return redirect(url_for("dash.dashboard"))
        
    return render_template("dashboard.html", user=current_user, messages=formatted_messages, dentists=dentists)