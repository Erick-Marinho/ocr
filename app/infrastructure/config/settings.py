from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    db_alembic_url: str

    debug: bool = False
    log_level: str = "INFO"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()