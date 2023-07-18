from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from config import settings


def create_app() -> FastAPI:
    app = FastAPI(docs_url="/", title=settings.APP_NAME)

    register_tortoise(
        app,
        db_url=get_db_url(
            user=settings.POSTGRESQL_USERNAME,
            passwd=settings.POSTGRESQL_PASSWORD,
            host=settings.POSTGRESQL_HOSTNAME,
            port=settings.POSTGRESQL_PORT,
            db=settings.POSTGRESQL_DATABASE
        ),
        modules={"models": ["models.Rate"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
    return app


def get_db_url(user, passwd, port, host, db):
    return f"postgres://{user}:{passwd}@{host}:{port}/{db}"
