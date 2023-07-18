from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Intern App"


settings = Settings()
