from flask import Blueprint, request, jsonify, session
from flask_login import login_required, current_user
from .models import Chat, db
import openai


bot = Blueprint("bot", __name__)


@bot.route("/chat", methods=["POST", "DELETE"])
@login_required
def chat():
    user_id = current_user.id

    if request.method == "DELETE":
        Chat.query.filter_by(user_id=user_id).delete()
        db.session.commit()
        return jsonify({"success": "All messages deleted"}), 200

    message = request.json.get('message')

    if not message:
        return jsonify({"error":"No message provided"})

    # Store user message
    user_message = Chat(user_id=user_id, role="user", content=message)
    db.session.add(user_message)
    db.session.commit()

    completion = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a knowledgeable and friendly dental assistant. Your responses should provide clear, accurate, and empathetic guidance on dental health topics. Aim to be supportive and encouraging while addressing user questions and concerns."},
            {"role": "user", "content": message}
        ]
    )
    response = completion.choices[0].message['content']

    # Store bot response
    bot_message = Chat(user_id=user_id, role="bot", content=response)
    db.session.add(bot_message)
    db.session.commit()
    
    return jsonify({"response":response})