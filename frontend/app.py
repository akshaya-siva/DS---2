import streamlit as st
from components.charts import plot_metrics_chart, plot_comparison_chart
import requests

# Title and Description
st.title("Model Comparison Dashboard")
st.markdown("An interactive dashboard to visualize model performance and make predictions.")

# Sidebar for navigation
page = st.sidebar.selectbox("Select Page", ["Model Performance", "Make Predictions"])

if page == "Model Performance":
    st.header("Model Performance Metrics")

    # Metrics for Default Models
    metrics_default = {
        "Logistic Regression": {
            "Precision": [0.80, 0.78],
            "Recall": [1.00, 0.02],
            "F1 Score": [0.89, 0.03],
            "Accuracy": [0.80]
        },
        "Decision Tree": {
            "Precision": [0.81, 0.28],
            "Recall": [0.84, 0.24],
            "F1 Score": [0.83, 0.25],
            "Accuracy": [0.72]
        },
        "Random Forest": {
            "Precision": [0.82, 0.32],
            "Recall": [0.89, 0.20],
            "F1 Score": [0.85, 0.25],
            "Accuracy": [0.75]
        },
        "CatBoost": {
            "Precision": [0.80, 0.72],
            "Recall": [1.00, 0.03],
            "F1 Score": [0.89, 0.06],
            "Accuracy": [0.80]
        },
        "Gradient Boosting": {
            "Precision": [0.80, 0.80],
            "Recall": [1.00, 0.01],
            "F1 Score": [0.89, 0.01],
            "Accuracy": [0.80]
        }
    }

    # Metrics for Tuned Models
    metrics_tuned = {
        "Logistic Regression": {
            "Precision": [0.87, 0.28],
            "Recall": [0.58, 0.65],
            "F1 Score": [0.69, 0.39],
            "Accuracy": [0.59]
        },
        "Decision Tree": {
            "Precision": [0.84, 0.29],
            "Recall": [0.71, 0.46],
            "F1 Score": [0.77, 0.36],
            "Accuracy": [0.66]
        },
        "Random Forest": {
            "Precision": [0.85, 0.28],
            "Recall": [0.65, 0.55],
            "F1 Score": [0.74, 0.37],
            "Accuracy": [0.63]
        },
        "CatBoost": {
            "Precision": [0.80, 0.73],
            "Recall": [1.00, 0.03],
            "F1 Score": [0.89, 0.06],
            "Accuracy": [0.80]
        },
        "Gradient Boosting": {
            "Precision": [0.80, 0.52],
            "Recall": [0.99, 0.05],
            "F1 Score": [0.89, 0.09],
            "Accuracy": [0.80]
        }
    }

    # Display Default Model Metrics
    st.subheader("Default Model Metrics")
    for model_name in metrics_default.keys():
        st.write(f"### {model_name}")
        plot_metrics_chart(metrics_default[model_name])

    # Display Tuned Model Metrics
    st.subheader("Tuned Model Metrics")
    for model_name in metrics_tuned.keys():
        st.write(f"### {model_name}")
        plot_metrics_chart(metrics_default[model_name])

    # Comparison of Default vs Tuned Models
    st.subheader("Comparison of Default vs Tuned Models")
    for model_name in metrics_default.keys():
        st.write(f"### {model_name}")
        plot_comparison_chart(metrics_default[model_name], metrics_tuned[model_name])

elif page == "Make Predictions":
    st.header("Make Predictions")

    # Select Model for Prediction
    model = st.selectbox('Select Model', [
        'Logistic Regression', 
        'Decision Tree', 
        'Random Forest', 
        'CatBoost', 
        'Gradient Boosting'
    ])

    # Input Features
    feature_1 = st.number_input('Feature 1')
    feature_2 = st.number_input('Feature 2')
    feature_3 = st.number_input('Feature 3')

    # Prediction Button
    if st.button('Predict'):
        response = requests.post(
            'http://127.0.0.1:8000/api/predictions/predict', 
            json={
                'model_name': model.lower().replace(' ', '_'),
                'features': [feature_1, feature_2, feature_3]
            }
        )
        
        if response.status_code == 200:
            result = response.json()
            st.success(f"Prediction: {result['prediction']}")
        else:
            st.error("Error in prediction")
