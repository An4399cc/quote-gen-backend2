from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # Cho phép truy cập từ frontend

quotes = [
    "Believe you can and you're halfway there.",
    "Do not wait to strike till the iron is hot; but make it hot by striking.",
    "The future belongs to those who prepare for it today.",
    "Your time is limited, don’t waste it living someone else’s life.",
    "The best way to predict the future is to create it."
]

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Quote Generator API"})

@app.route('/generate', methods=['GET'])
def generate_quote():
    quote = random.choice(quotes)
    return jsonify({"quote": quote})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
