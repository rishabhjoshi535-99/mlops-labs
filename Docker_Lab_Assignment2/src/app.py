from flask import Flask, jsonify, request
from utils import validate_number_input, format_prediction_response
import random
import os

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Docker Lab Assignment 2 - Flask Service is running",
        "service": "number-classifier",
        "version": "1.0.0"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "environment": os.getenv("ENVIRONMENT", "development")
    })


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    number = validate_number_input(data)

    # Simulated business logic
    category = "even" if number % 2 == 0 else "odd"

    # Simulated confidence (to make it look production-like)
    confidence = round(random.uniform(0.85, 0.99), 2)

    return jsonify(format_prediction_response(number, category, confidence))
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

