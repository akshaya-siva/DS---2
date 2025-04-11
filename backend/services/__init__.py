"""
Services Package Initialization
===============================
This package contains business logic and helper functions for the backend application. The services are modularized to handle specific functionalities, such as loading machine learning models and making predictions.

Modules:
--------
- model_service.py: Contains logic for loading models and making predictions.
- preprocessing_service.py: Contains data preprocessing logic (e.g., scaling, encoding).

Usage:
------
Import services into route files or other parts of the backend application.

Example:
--------
from services.model_service import load_model, predict_with_model
from services.preprocessing_service import preprocess_data

model = load_model("random_forest")
processed_data = preprocess_data(input_features)
prediction = predict_with_model(model, processed_data)
"""

# Import necessary modules for service initialization
import os
import sys

# Add the backend directory to sys.path to ensure imports work correctly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

# Initialize the package
__all__ = [
    "model_service",
    "preprocessing_service"
]
