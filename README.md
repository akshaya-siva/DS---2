# Medical Appointment No-Show Prediction

Can we know if a patient won’t show up before the appointment?

🧠Project in a Nutshell

Every missed appointment wastes time, money, and resources. This project uses machine learning to predict whether a patient will skip their medical appointment based on historical and demographic data.

We analyzed, modeled, and fine-tuned multiple ML algorithms to tackle this real-world healthcare problem.

Data Source: Public dataset from Brazilian medical appointments (Kaggle)

---

🚀 What’s Inside

✅ Data Preprocessing

✅ Exploratory Data Analysis (EDA)

✅ Model Training (5 Classifiers)

✅ Hyperparameter Tuning (RandomizedSearchCV)

✅ Model Evaluation & Comparison

✅ All Models Saved as Pickle Files

Technologies

Python, Pandas, NumPy

Scikit-learn, CatBoost

Matplotlib, Seaborn

RandomizedSearchCV for Tuning

Pickle for Model Persistence

# 📊 Data Science Workflow

📦 Data Cleaning

Converted "No-show" column into binary (yes = 1, no = 0)

Dropped irrelevant fields like PatientID, AppointmentID

Checked class balance and handled missing values

🔍 EDA

Visualized no-show rates

Heatmaps to uncover correlations

Class distribution plots

🤖 Model Building

We trained 5 different models:

Logistic Regression

Decision Tree

Random Forest

CatBoost

Gradient Boosting

Then we performed RandomizedSearchCV to tune them and saved both default & tuned versions.

🔍 4. Model Explainability

We chose interpretable models like Logistic Regression and Decision Trees

Tracked how performance changed before and after tuning

Used classification_report for easy metric comparison

---


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
frontend/
    app.py                     # Streamlit dashboard application
    components/
        charts.py              # Functions for creating charts
    hidden_pages/
        performance_page.py    # Page for visualizing model performance
        prediction_page.py     # Page for making predictions
    assets/
        style.css              # Custom styles for the dashboard
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

## Frontend Description

The frontend is a **Streamlit-based dashboard** that provides an interactive interface for users to:

- **Visualize Model Performance**: View charts and metrics for different machine learning models.
- **Make Predictions**: Input features and get predictions from the backend API.
- **Multi-Page Support**: Navigate between pages for performance visualization and prediction.

### Key Components

- **`app.py`**: The main entry point for the Streamlit application.
- **`components/charts.py`**: Contains reusable functions for creating charts (e.g., bar charts, line charts).
- **`hidden_pages/performance_page.py`**: Displays model performance metrics and visualizations.
- **`hidden_pages/prediction_page.py`**: Allows users to input features and make predictions via the backend API.
- **`assets/style.css`**: Custom CSS for styling the dashboard.

### Frontend Setup

1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```

2. Install dependencies using `pipenv`:
   ```bash
   pipenv install
   ```

3. Activate the virtual environment:
   ```bash
   pipenv shell
   ```

4. Run the Streamlit dashboard:
   ```bash
   pipenv run streamlit run app.py
   ```

5. Access the dashboard in your browser at:
   - [http://localhost:8501](http://localhost:8501)

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

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
