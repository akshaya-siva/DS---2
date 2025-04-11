"""
Tests Package Initialization
============================
This package contains unit tests for the backend application. The tests are organized into modules
that correspond to different components of the backend, such as routes and services.

Modules:
--------
- test_routes.py: Contains unit tests for API route endpoints.
- test_services.py: Contains unit tests for business logic and helper functions.
- test_models.py: Contains unit tests for machine learning model loading and predictions.

Usage:
------
Run all tests using pytest:
    $ pytest tests/

Run specific test files:
    $ pytest tests/test_routes.py

Run specific test functions:
    $ pytest tests/test_routes.py::test_health_check
"""

# Import necessary modules for testing
import os
import sys

# Add the backend directory to sys.path to ensure imports work correctly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

# Initialize the package
__all__ = [
    "test_routes",
    "test_services",
    "test_models"
]
