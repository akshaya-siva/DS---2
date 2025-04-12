import streamlit as st
from components.charts import plot_metrics_chart, plot_comparison_chart
import requests
import os
import sys

from st_pages import hide_pages, Page

# path_pages=os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))+'/frontend/pages/'
# print(path_pages)
# Title and Description
st.title("Model Comparison Dashboard")
st.markdown("An interactive dashboard to visualize model performance and make predictions.")
# hide_pages([Page(os.path.join(path_pages,"__init__.py")), Page(os.path.join(path_pages,"performance_page.py")),Page(os.path.join(path_pages,"prediction_page.py"))])

# Sidebar for navigation
page = st.sidebar.selectbox("Select Page", ["Model Performance", "Make Predictions"])
st.markdown(
    """<style>
        @import url('assets/style.css');
        body { font-family: 'Arial', sans-serif; }
        h1 { color: #007bff; }
        /* Additional styles here if needed */
    </style>
    """,
    unsafe_allow_html=True
)


if page == "Model Performance":
    
    st.header("Model Performance Metrics")
    metrics_before_tuning = {
        "Accuracy": [0.85, 0.88, 0.89, 0.87, 0.90],
        "Precision": [0.83, 0.86, 0.87, 0.84, 0.88],
        "Recall": [0.80, 0.84, 0.85, 0.82, 0.87],
        "F1 Score": [0.81, 0.85, 0.86, 0.83, 0.89],
    }
    metrics_after_tuning = {
        "Accuracy": [0.88, 0.91, 0.92, 0.90, 0.93],
        "Precision": [0.86, 0.89, 0.90, 0.87, 0.91],
        "Recall": [0.84, 0.87, 0.88, 0.85, 0.89],
        "F1 Score": [0.85, 0.88, 0.89, 0.86, 0.92],
    }
    # models = ["Logistic Regression", "Random Forest", "Gradient Boosting"]
    models = ["Catboost", "Random Forest", "Gradient Boosting","Decision Tree","Logistic Regression"]

    st.subheader("Before Fine-Tuning")
    plot_metrics_chart(metrics_before_tuning, models)
    
    st.subheader("After Fine-Tuning")
    plot_metrics_chart(metrics_after_tuning, models)
    
    st.subheader("Comparison of Metrics")
    plot_comparison_chart(metrics_before_tuning, metrics_after_tuning, models)

elif page == "Make Predictions":
    st.header("Make Predictions")
    # model = st.selectbox('Select Model', ['Logistic Regression', 'Random Forest', 'Gradient Boosting'])
    model = st.selectbox('Select Model', ['Logistic Regression', 'Random Forest', 'Gradient Boosting','Catboost','Decision Tree'])

    feature_1 = st.number_input('Feature 1')
    feature_2 = st.number_input('Feature 2')
    feature_3 = st.number_input('Feature 3')

    if st.button('Predict'):
        response = requests.post('http://127.0.0.1:8000/api/predictions/predict', json={
            'model_name': model.lower().replace(' ', '_'),
            'features': [feature_1, feature_2, feature_3]
        })
        
        if response.status_code == 200:
            result = response.json()
            st.success(f"Prediction: {result['prediction']}")
        else:
            st.error("Error in prediction")
