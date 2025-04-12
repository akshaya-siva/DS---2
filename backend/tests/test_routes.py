from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_health_check():
    response = client.get("/api/health/")
    assert response.status_code == 200
    assert response.json() == {"status": "Healthy"}

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Model Comparison API!"}

def test_prediction_endpoint():
    payload = {
        "model_name": "logistic_model",
        "features": [25, 1, 0, 3]
    }
    response = client.post("/api/predictions/predict", json=payload)
    assert response.status_code == 200
