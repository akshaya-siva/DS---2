"""
Routes Package Initialization
===============================
This package contains API route definitions for the backend application. The routes are organized into modules
that handle specific functionalities, such as predictions and health checks.

Modules:
--------
- prediction_routes.py: Contains API endpoints for model predictions.
- health_routes.py: Contains health check endpoints to verify the backend status.

Usage:
------
Import routes into the main application file (`app.py`) and include them using FastAPI's router mechanism.

Example:
--------
from routes.prediction_routes import router as prediction_router
from routes.health_routes import router as health_router

app.include_router(prediction_router, prefix="/api/predictions", tags=["Predictions"])
app.include_router(health_router, prefix="/api/health", tags=["Health"])
"""

# Import necessary modules for route initialization
import os
import sys

# Add the backend directory to sys.path to ensure imports work correctly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

# Initialize the package
__all__ = [
    "prediction_routes",
    "health_routes"
]
