"""
evaluate.py

This script evaluates the trained Logistic Regression model
on the Iris dataset using accuracy as the evaluation metric.

The purpose is to keep evaluation simple and transparent,
so the focus remains on understanding the MLOps workflow
rather than model tuning.
"""

import joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def evaluate_model():
    # Load the Iris dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Split the data (same split settings as training for consistency)
    _, X_test, _, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Load the trained model
    model = joblib.load("model.joblib")

    # Make predictions
    y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)

    print(f"Model evaluation completed.")
    print(f"Accuracy on test set: {accuracy:.4f}")


if __name__ == "__main__":
    evaluate_model()
