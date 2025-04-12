import streamlit as st
import requests

def render_prediction_page():
    """
    Renders the Make Predictions page.
    """
    st.header("Make Predictions")
    
    model = st.selectbox('Select Model', ['Logistic Regression', 'Random Forest', 'Gradient Boosting'])
    
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
