import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class Config:
    """
    Configuration class for managing application settings.
    """
    # Application settings
    APP_NAME = "Model Comparison API"
    DEBUG = os.getenv("DEBUG", True)  # Debug mode (default: True)
    HOST = os.getenv("HOST", "0.0.0.0")  # Host address
    PORT = int(os.getenv("PORT", 8000))  # Port number

    # Paths
    MODEL_DIRECTORY = os.getenv("MODEL_DIRECTORY", "./models")  # Path to saved models
    LOG_DIRECTORY = os.getenv("LOG_DIRECTORY", "./logs")  # Path to log files

    # Database configuration (if applicable)
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = int(os.getenv("DB_PORT", 5432))
    DB_NAME = os.getenv("DB_NAME", "model_comparison_db")
    DB_USER = os.getenv("DB_USER", "admin")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "password")

    # Security settings
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")

    # Other settings
    ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "*").split(",")  # CORS origins

# Access configuration settings using `Config.<attribute>`
