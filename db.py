from tortoise import Tortoise
import config


async def init_db():
    await Tortoise.init(
        db_url=f'postgres://{config.POSTGRES_USERNAME}:{config.POSTGRES_PASSWORD}@localhost:5432/{config.POSTGRES_DB}',
        modules={'models': ['models']},
    )


async def close_db():
    await Tortoise.close_connections()
