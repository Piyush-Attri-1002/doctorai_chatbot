# app.py

# Import Flask tools and chatbot logic
from flask import Flask, render_template, request
from chatbot_logic import get_response  # Function we’ll write next

# Create the Flask web app
app = Flask(__name__)

# Set the homepage route
@app.route("/", methods=["GET", "POST"])
def index():
    user_input = ""     # Stores user's input text
    bot_response = ""   # Stores chatbot's reply

    # When user submits the form
    if request.method == "POST":
        user_input = request.form["user_input"]
        bot_response = get_response(user_input)

    # Render the webpage with responses
    return render_template("index.html", user_input=user_input, bot_response=bot_response)

# Start the app
if __name__ == "__main__":
    print("✅ Chatbot Flask app is starting...")
    app.run(debug=True)
