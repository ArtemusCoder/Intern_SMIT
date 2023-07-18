from fastapi import FastAPI
from config import settings



def create_app() -> FastAPI:
    app = FastAPI(docs_url="/", title=settings.APP_NAME)

    return app