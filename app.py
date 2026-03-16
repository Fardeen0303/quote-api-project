from flask import Flask
import random

app = Flask(__name__)

quotes = [
    "Stay hungry stay foolish",
    "Talk is cheap show me the code",
    "Programs must be written for people to read"
]

@app.route("/")
def home():
    return {"quote": random.choice(quotes)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
