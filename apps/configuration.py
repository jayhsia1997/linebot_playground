"""
Environment configuration
"""
import os
from typing import List, Optional

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Configuration(BaseSettings):
    """Configuration"""

    APP_NAME: str = "apps"
    ENV: str = os.getenv("ENV", "dev")

    # CORS
    CORS_ALLOWED_ORIGINS: Optional[List[str]] = os.getenv(key="CORS_ALLOWED_ORIGINS")
    CORS_EXPOSE_HEADERS: Optional[List[str]] = os.getenv(key="CORS_EXPOSE_HEADERS")
    CORS_ALLOW_ORIGINS_REGEX: Optional[str] = os.getenv(key="CORS_ALLOW_ORIGINS_REGEX")

    # Line
    LINE_CHANNEL_SECRET: str = os.getenv(key="LINE_CHANNEL_SECRET")
    LINE_CHANNEL_ACCESS_TOKEN: str = os.getenv(key="LINE_CHANNEL_ACCESS_TOKEN")

    # Redis
    REDIS_HOST: str = os.getenv(key="REDIS_HOST")
    REDIS_PORT: int = os.getenv(key="REDIS_PORT")
    REDIS_PASSWORD: str = os.getenv(key="REDIS_PASSWORD")
    REDIS_DB: int = os.getenv(key="REDIS_DB")
    REDIS_SSL: bool = os.getenv(key="REDIS_SSL")


settings = Configuration()
