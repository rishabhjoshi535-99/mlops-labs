# Docker Lab Assignment 2

# Flask-Based Number Classification Microservice

## Rishabh Joshi
## MS Data Analytics Engineering
## Northeastern University

## 1. Introduction:

This lab implements a containerized Flask-based REST microservice that classifies a given number as even or odd.

The application is developed using Python and Flask and is deployed inside a Docker container to ensure portability and reproducibility.

The service exposes endpoints for:

- Health monitoring

- Number classification

## 2. Technology Stack

- Python 3.10
- Flask
- Docker

## 3. Project Structure

Docker_Lab_Assignment2/
│
├── Dockerfile
├── requirements.txt
└── src/
    ├── app.py
    └── utils.py

## 4. How to Re-run the Lab: All commands must be executed inside the Docker_Lab_Assignment2 directory.

### Step 1: Build Docker Image
docker build -t docker-lab-assignment2:v1 .

### Step 2: Run Container: docker run -d -p 5002:5000 docker-lab-assignment2:v1

This maps:

- Local port 5002
- To container port 5000

### Step 3: Verify Container: docker ps

## 5. API Endpoints:

### 5.1 Health Check: curl http://localhost:5002/health

Expected Output:
{
  "environment": "development",
  "status": "healthy"
}

### 5.2 Number Classification:

Example request:
curl -X POST http://localhost:5002/predict \
  -H "Content-Type: application/json" \
  -d '{"name":"8"}'

Expected Response: {
  "category": "even",
  "confidence": 0.91,
  "input": 8
}

Odd Number Example:

curl -X POST http://localhost:5002/predict \
  -H "Content-Type: application/json" \
  -d '{"name":"5"}'

Expected Response:

{
  "category": "odd",
  "confidence": 0.88,
  "input": 5
}

## 6. Implementation Details

- Input validation is handled inside utils.py
- Input is explicitly converted from string to integer before classification
- Even/odd logic uses the modulus operator: number % 2 == 0
- A simulated confidence score is generated between 0.85 and 0.99

## 7. Docker Configuration:

The Dockerfile:

- Uses python:3.10-slim
- Installs dependencies from requirements.txt
- Copies application source code
- Exposes port 5000
- Runs the application using: CMD ["python", "app.py"]

## 8. Stopping the Container

- To stop the running container: docker stop <container_id>

- Or remove all containers: docker rm -f $(docker ps -aq)

## 9. Conclusion:

The lab demonstrates:

- REST API development using Flask
- Containerization using Docker
- Proper documentation for reproducibility
- Validation and structured response handling

The application was successfully tested using curl requests and verified through Docker container execution.
