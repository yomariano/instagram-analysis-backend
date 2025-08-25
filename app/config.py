import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Optional settings that won't cause startup failures
    database_url: str = os.getenv("DATABASE_URL", "")
    redis_url: str = os.getenv("REDIS_URL", "")
    apify_token: str = os.getenv("APIFY_TOKEN", "")
    gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")
    secret_key: str = os.getenv("SECRET_KEY", "your-secret-key")
    allowed_origins: str = os.getenv("CORS_ALLOWED_ORIGINS", os.getenv("ALLOWED_ORIGINS", "https://instagram-app.teabag.online,http://localhost:3000"))
    
    class Config:
        env_file = ".env"

settings = Settings()