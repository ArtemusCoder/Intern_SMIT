from tortoise import Tortoise, run_async
from config import get_db_url, settings


async def main():
    await Tortoise.init(
        db_url=get_db_url(
            user=settings.POSTGRESQL_USERNAME,
            passwd=settings.POSTGRESQL_PASSWORD,
            host=settings.POSTGRESQL_HOSTNAME,
            port=settings.POSTGRESQL_PORT,
            db=settings.POSTGRESQL_DATABASE
        ),
        modules={'models': ['models.Rate']}
    )
    await Tortoise.generate_schemas()


if __name__ == '__main__':
    run_async(main())
