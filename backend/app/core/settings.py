from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[3]


class Settings(BaseSettings):

    frontend_url: str
    database_url: str
    backend_port: int

    jwt_algorithm: str
    jwt_private_key: str
    jwt_public_key: str
    access_token_expire_minutes: int
    refresh_token_expire_days: int
    resend_api_key: str
    redis_server_url: str
    debug: bool = False

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env", env_file_encoding="utf-8", extra="ignore"
    )


settings = Settings()
