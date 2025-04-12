from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import numpy as np
from services.model_service import load_model, predict_with_model

router = APIRouter()

# Define input schema for prediction requests
class PredictionInput(BaseModel):
    model_name: str  # Name of the model to use (e.g., "logistic_model")
    features: list   # List of input features for prediction

@router.post("/predict")
def predict(input_data: PredictionInput):
    model_name = input_data.model_name.lower()
    features = np.array(input_data.features).reshape(1, -1)

    try:
        model = load_model(model_name)
        prediction = predict_with_model(model, features)
        return {"model_name": model_name, "prediction": int(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error during prediction: {str(e)}")
 