"""
Components Package Initialization
=================================
This package contains reusable UI components for the dashboard application. These components are modularized to handle specific functionalities, such as creating charts and visualizations.

Modules:
--------
- charts.py: Contains functions to create performance charts (e.g., bar charts, line graphs).

Usage:
------
Import components into other parts of the frontend application.

Example:
--------
from components.charts import plot_metrics_chart, plot_comparison_chart

plot_metrics_chart(metrics, models)
plot_comparison_chart(metrics_before_tuning, metrics_after_tuning, models)
"""

# Import necessary modules for component initialization
import os
import sys

# Add the frontend directory to sys.path to ensure imports work correctly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

# Initialize the package
__all__ = [
    "charts"
]
