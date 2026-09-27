from flask import Flask, request, jsonify, render_template
from router import detect_intent
from context_engine import ContextEngine

import modules.study as study
import modules.productivity as productivity
import modules.resume as resume

app = Flask(__name__)
context_engine = ContextEngine()


# 🔥 Home Route (Add Above /chat)
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    intent, confidence = detect_intent(user_input)
    final_intent = context_engine.resolve_intent(intent, confidence)

    if final_intent == "clarify":
        return jsonify({"response": "Can you clarify what you mean?"})

    if final_intent == "study":
        response = study.handle(user_input)

    elif final_intent == "productivity":
        response = productivity.handle(user_input)

    elif final_intent == "resume":
        response = resume.handle(user_input)

    else:
        response = "Sorry, I don’t understand."

    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)