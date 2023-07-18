from pydantic import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    APP_NAME: str = "Intern App"
    POSTGRESQL_HOSTNAME: str = os.environ.get("DB_HOST")
    POSTGRESQL_PORT: str = os.environ.get("DB_PORT")
    POSTGRESQL_USERNAME: str = os.environ.get("DB_USER")
    POSTGRESQL_PASSWORD: str = os.environ.get("DB_PASSWORD")
    POSTGRESQL_DATABASE: str = os.environ.get("DB_NAME")

settings = Settings()
