from fastapi import FastAPI
from routes.prediction_routes import router as prediction_router
from routes.health_routes import router as health_router

# Initialize FastAPI app
app = FastAPI(
    title="Model Comparison API",
    description="API to serve machine learning model predictions and health checks",
    version="1.0.0"
)

# Include routers for different endpoints
app.include_router(prediction_router, prefix="/api/predictions", tags=["Predictions"])
app.include_router(health_router, prefix="/api/health", tags=["Health"])

@app.get("/")
def root():
    return {"message": "Welcome to the Model Comparison API!"}
