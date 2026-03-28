import mlflow
import mlflow.sklearn
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Step 1: Create simple dataset (from scratch)
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# Step 2: Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Start MLflow run
with mlflow.start_run():

    # Step 4: Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Step 5: Predict
    predictions = model.predict(X_test)

    # Step 6: Calculate metric
    mse = mean_squared_error(y_test, predictions)

    # Step 7: Log parameter
    mlflow.log_param("model_type", "LinearRegression")

    # Step 8: Log metric
    mlflow.log_metric("mse", mse)

    # Step 9: Log model
    mlflow.sklearn.log_model(model, "model")

    print("Model trained and logged successfully!")
