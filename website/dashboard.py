from flask import Blueprint, render_template, request, jsonify
from flask_login import current_user, login_required
from .models import Chat, db


dash = Blueprint("dash", __name__)

@dash.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    user_id = current_user.id
    messages = Chat.query.filter_by(user_id=user_id).order_by(Chat.timestamp).all()
    formatted_messages = [{"role": message.role, "content": message.content} for message in messages]
    return render_template("dashboard.html", user=current_user, messages=formatted_messages)