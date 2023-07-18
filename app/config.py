from dotenv import load_dotenv
import os
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    APP_NAME: str = "Intern App"
    POSTGRESQL_HOSTNAME: str = os.environ.get("DB_HOST")
    POSTGRESQL_PORT: str = os.environ.get("DB_PORT")
    POSTGRESQL_USERNAME: str = os.environ.get("DB_USER")
    POSTGRESQL_PASSWORD: str = os.environ.get("DB_PASSWORD")
    POSTGRESQL_DATABASE: str = os.environ.get("DB_NAME")

def get_db_url(user, passwd, port, host, db):
    return f"postgres://{user}:{passwd}@{host}:{port}/{db}"

settings = Settings()
