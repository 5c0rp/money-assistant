import secrets

from pydantic import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = True
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)

    class Config:
        case_sensitive = True


settings = Settings()
