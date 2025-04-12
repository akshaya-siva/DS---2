import streamlit as st
from components.charts import plot_metrics_chart

def render_performance_page():
    """
    Renders the Model Performance page.
    """
    st.header("Model Performance Metrics")
    
    metrics_before_tuning = {
        "Accuracy": [0.85, 0.88, 0.89, 0.87, 0.90],
        "Precision": [0.83, 0.86, 0.87, 0.84, 0.88],
        "Recall": [0.80, 0.84, 0.85, 0.82, 0.87],
        "F1 Score": [0.81, 0.85, 0.86, 0.83, 0.89],
    }
    
    models = ["Catboost", "Random Forest", "Gradient Boosting","Decision Tree","Logistic Regression"]
    
    plot_metrics_chart(metrics_before_tuning, models)
