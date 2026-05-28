import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Application
    app_name: str = os.getenv('APP_NAME', 'pingpong-ai-counter')
    app_env: str = os.getenv('APP_ENV', 'development')
    debug: bool = os.getenv('DEBUG', 'False').lower() == 'true'
    
    # API
    api_host: str = os.getenv('API_HOST', '0.0.0.0')
    api_port: int = int(os.getenv('API_PORT', '8000'))
    api_reload: bool = os.getenv('API_RELOAD', 'True').lower() == 'true'
    cors_origins: str = os.getenv('CORS_ORIGINS', '["http://localhost:3000", "http://localhost:8080"]')
    
    # Azure
    azure_subscription_id: str = os.getenv('AZURE_SUBSCRIPTION_ID', '')
    azure_resource_group: str = os.getenv('AZURE_RESOURCE_GROUP', '')
    azure_region: str = os.getenv('AZURE_REGION', 'westeurope')
    
    # Storage
    azure_storage_account: str = os.getenv('AZURE_STORAGE_ACCOUNT', '')
    azure_storage_connection_string: str = os.getenv('AZURE_STORAGE_CONNECTION_STRING', '')
    
    # Cosmos DB
    azure_cosmos_connection_string: str = os.getenv('AZURE_COSMOS_CONNECTION_STRING', '')
    
    # SignalR
    signalr_connection_string: str = os.getenv('SIGNALR_CONNECTION_STRING', '')
    
    # ML
    azure_ml_workspace: str = os.getenv('AZURE_ML_WORKSPACE', '')
    azure_ml_subscription: str = os.getenv('AZURE_ML_SUBSCRIPTION', '')
    
    # Container Registry
    acr_name: str = os.getenv('ACR_NAME', '')
    acr_login_server: str = os.getenv('ACR_LOGIN_SERVER', '')
    acr_username: str = os.getenv('ACR_USERNAME', '')
    acr_password: str = os.getenv('ACR_PASSWORD', '')
    
    # Model
    model_path: str = os.getenv('MODEL_PATH', './models/trained/')
    model_name: str = os.getenv('MODEL_NAME', 'pingpong-detector')
    model_version: str = os.getenv('MODEL_VERSION', '1.0')
    
    # YOLO
    yolo_confidence_threshold: float = float(os.getenv('YOLO_CONFIDENCE_THRESHOLD', '0.5'))
    yolo_iou_threshold: float = float(os.getenv('YOLO_IOU_THRESHOLD', '0.5'))
    yolo_image_size: int = int(os.getenv('YOLO_IMAGE_SIZE', '640'))
    yolo_epochs: int = int(os.getenv('YOLO_EPOCHS', '50'))
    yolo_batch_size: int = int(os.getenv('YOLO_BATCH_SIZE', '16'))
    
    # Training Data
    training_data_path: str = os.getenv('TRAINING_DATA_PATH', './data/training/')
    training_data_split: float = float(os.getenv('TRAINING_DATA_SPLIT', '0.7'))
    validation_data_split: float = float(os.getenv('VALIDATION_DATA_SPLIT', '0.15'))
    test_data_split: float = float(os.getenv('TEST_DATA_SPLIT', '0.15'))
    
    # Video
    video_fps: int = int(os.getenv('VIDEO_FPS', '30'))
    video_frame_skip: int = int(os.getenv('VIDEO_FRAME_SKIP', '0'))
    video_confidence: float = float(os.getenv('VIDEO_CONFIDENCE', '0.5'))
    
    # Player Detection
    jersey_color_1: str = os.getenv('JERSEY_COLOR_1', 'red')
    jersey_color_2: str = os.getenv('JERSEY_COLOR_2', 'blue')
    player_detection_confidence: float = float(os.getenv('PLAYER_DETECTION_CONFIDENCE', '0.6'))
    
    # Logging
    log_level: str = os.getenv('LOG_LEVEL', 'INFO')
    log_format: str = os.getenv('LOG_FORMAT', '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log_file: str = os.getenv('LOG_FILE', './logs/app.log')
    
    class Config:
        env_file = '.env'
        case_sensitive = False
        extra = 'allow'

settings = Settings()