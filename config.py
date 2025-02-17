# app/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://username:password@localhost:5432/bookstore_db"

    class Config:
        env_file = ".env"  # Load environment variables from a .env file if available

settings = Settings()
