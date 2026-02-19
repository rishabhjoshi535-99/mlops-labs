from utils import vaidate_input, generate_response
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

    number = validate_input(data.get("name", ""))

    # Simulated business logic
    category = "even" if number % 2 == 0 else "odd"

    # Simulated confidence (to make it look production-like)
    confidence = round(random.uniform(0.85, 0.99), 2)

    return jsonify(generate_response(data.get("name", "")))
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

