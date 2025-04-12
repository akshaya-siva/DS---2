import streamlit as st
from components.charts import plot_metrics_chart, plot_comparison_chart

def render_performance_page():
    """
    Renders the Model Performance page.
    """
    st.header("Model Performance Metrics")

    # Metrics Before Tuning
    metrics_before_tuning = {
        "Accuracy": [0.80, 0.72, 0.75, 0.80, 0.80],
        "Precision": [0.80, 0.81, 0.82, 0.80, 0.80],
        "Recall": [1.00, 0.84, 0.89, 1.00, 1.00],
        "F1 Score": [0.89, 0.83, 0.85, 0.89, 0.89],
    }

    # Metrics After Tuning
    metrics_after_tuning = {
        "Accuracy": [0.59, 0.66, 0.63, 0.80, 0.80],
        "Precision": [0.87, 0.84, 0.85, 0.80, 0.80],
        "Recall": [0.58, 0.71, 0.65, 1.00, 0.99],
        "F1 Score": [0.69, 0.77, 0.74, 0.89, 0.89],
    }

    # Models List
    models = ["Logistic Regression", "Decision Tree", "Random Forest", "CatBoost", "Gradient Boosting"]

    # Render Metrics Before Tuning
    st.subheader("Metrics Before Tuning")
    plot_metrics_chart(metrics_before_tuning, models)

    # Render Metrics After Tuning
    st.subheader("Metrics After Tuning")
    plot_metrics_chart(metrics_after_tuning, models)

    # Render Comparison Chart
    st.subheader("Comparison of Metrics Before and After Tuning")
    plot_comparison_chart(metrics_before_tuning, metrics_after_tuning, models)
