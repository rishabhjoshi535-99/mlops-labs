"""
train.py

This script trains a Logistic Regression model on the Iris dataset.
The focus is on keeping the training logic simple and easy to follow,
since the primary goal of this lab is to demonstrate ML automation
using GitHub Actions rather than model optimization.
"""

import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


def train_model():
    # Load the Iris dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Initialize the Logistic Regression model
    model = LogisticRegression(max_iter=200)

    # Train the model
    model.fit(X_train, y_train)

    # Save the trained model
    joblib.dump(model, "model.joblib")

    print("Model training completed successfully.")
    print("Model saved as model.joblib")


if __name__ == "__main__":
    train_model()
