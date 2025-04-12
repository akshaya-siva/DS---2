"""
Pages Package Initialization
===============================
This package contains modularized pages for the dashboard application. Each page is designed to handle specific functionalities, such as visualizing model performance metrics or making predictions.

Modules:
--------
- performance_page.py: Contains logic for visualizing model performance metrics.
- prediction_page.py: Handles user input and integrates with backend APIs for predictions.

Usage:
------
Import pages into the main dashboard application file (`app.py`) and render them based on user selection.

Example:
--------
from pages.performance_page import render_performance_page
from pages.prediction_page import render_prediction_page

if page == "Model Performance":
    render_performance_page()
elif page == "Make Predictions":
    render_prediction_page()
"""

# Import necessary modules for page initialization
import os
import sys

# Add the frontend directory to sys.path to ensure imports work correctly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

# Initialize the package
__all__ = [
    "performance_page",
    "prediction_page"
]
