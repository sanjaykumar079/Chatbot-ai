from flask import Flask, request, render_template
from emotion_detector import detect_emotion
from response_generator import generate_response
from database import init_db, store_chat, get_chat_history

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def chat():
    init_db()
    if request.method == "POST":
        user_input = request.form["user_input"]
        emotion, score = detect_emotion(user_input)
        bot_response = generate_response(emotion, user_input)
        store_chat(user_input, emotion, bot_response)
        chat_history = get_chat_history()
        return render_template("chat.html", user_input=user_input, emotion=emotion, 
                             bot_response=bot_response, chat_history=chat_history)
    chat_history = get_chat_history()
    return render_template("chat.html", chat_history=chat_history)

if __name__ == "__main__":
    app.run(debug=True)