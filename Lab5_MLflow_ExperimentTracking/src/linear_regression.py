import mlflow
import mlflow.sklearn
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Set experiment name
mlflow.set_experiment("Lab5_LinearRegression_Experiment")

# Create slightly modified dataset
X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([3, 5, 7, 9, 11, 13])

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Start MLflow run with name
with mlflow.start_run(run_name="LinearRegression_Run"):

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict
    predictions = model.predict(X_test)

    # Metrics
    mse = mean_squared_error(y_test, predictions)
    rmse = np.sqrt(mse)

    # Log parameters
    mlflow.log_param("model_type", "LinearRegression")
    mlflow.log_param("dataset_size", len(X))

    # Log metrics
    mlflow.log_metric("mse", mse)
    mlflow.log_metric("rmse", rmse)

    # Log model
    mlflow.sklearn.log_model(model, "model")

    print("Experiment completed successfully!")
