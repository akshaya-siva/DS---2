import joblib

# Load a saved model from the models directory
def load_model(model_name: str):
    try:
        return joblib.load(f"models/{model_name}.pkl")
    except FileNotFoundError:
        raise Exception(f"Model '{model_name}' not found!")

# Make predictions using a given model and input features
def predict_with_model(model, features):
    return model.predict(features)
