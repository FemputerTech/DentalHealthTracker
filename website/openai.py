from flask import Blueprint, render_template, request, jsonify
import openai


bot = Blueprint("bot", __name__)


@bot.route("/chat", methods=["POST"])
def chat():
    message = request.json.get('message')

    if not message:
        return jsonify({"error":"No message provided"})
    
    completion = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a knowledgeable and friendly dental assistant. Your responses should provide clear, accurate, and empathetic guidance on dental health topics. Aim to be supportive and encouraging while addressing user questions and concerns."},
            {"role": "user", "content": message}
        ]
    )
    response = completion.choices[0].message['content']
    

    return jsonify({"response":response})