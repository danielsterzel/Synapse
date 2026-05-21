from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    frontend_url: str
    database_url: str
    backend_port: int

    jwt_algorithm: str
    jwt_private_key: str
    jwt_public_key: str


    debug: bool = False


    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()
