# Model Comparison API

This project provides a FastAPI-based backend for serving machine learning model predictions. It includes endpoints for making predictions using pre-trained models and is designed to be modular and extensible.

---

## Features

- **Prediction API**: Make predictions using pre-trained machine learning models.
- **Input Validation**: Ensures proper input format using Pydantic models.
- **Error Handling**: Returns meaningful error messages for invalid requests or issues during prediction.
- **Modular Design**: Organized structure for routes, services, and models.

---

## API Endpoints

### 1. **Prediction Endpoint**

- **URL**: `/api/predictions/predict`
- **Method**: `POST`
- **Description**: Predicts the output using the specified machine learning model and input features.

#### Request Body
```json
{
  "model_name": "logistic_model",
  "features": [1.5, 2.3, 3.1, 4.0]
}
```

- `model_name`: The name of the model to use (e.g., `logistic_model`, `random_forest`).
- `features`: A list of numerical input features for the model.

#### Response
```json
{
  "model_name": "logistic_model",
  "prediction": 1
}
```

- `model_name`: The name of the model used for prediction.
- `prediction`: The predicted output.

#### Error Response
If an error occurs during prediction (e.g., model not found or invalid input), the API returns:
```json
{
  "detail": "Error during prediction: <error_message>"
}
```

---

## Project Structure

```
backend/
    app.py                     # Main FastAPI application
    routes/
        prediction_routes.py   # Routes for prediction endpoints
    services/
        model_service.py       # Logic for loading models and making predictions
    models/
        logistic_model.pkl     # Pre-trained logistic regression model
        random_forest.pkl      # Pre-trained random forest model
    tests/
        test_routes.py         # Unit tests for API routes
```

---

## Installation

### Prerequisites

- Python 3.11+
- Pipenv for dependency management

### Steps

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd backend
   ```

2. Install dependencies using `pipenv`:
   ```bash
   pipenv install
   ```

3. Activate the virtual environment:
   ```bash
   pipenv shell
   ```

4. Run the FastAPI application:
   ```bash
   pipenv run uvicorn app:app --port 8000 --host '127.0.0.1' --reload
   ```

5. Access the API documentation:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Testing

1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```

2. Run the tests using `pytest`:
   ```bash
   pipenv run pytest tests/
   ```

---

## Notes

- Ensure the pre-trained models are placed in the `models/` directory.
- Add additional models by saving them as `.pkl` files and updating the `model_service.py` logic if needed.

---

