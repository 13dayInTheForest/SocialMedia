from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from src.core.config import settings
from .models import Base


async_engine = create_async_engine(settings.get_db_url, echo=True, pool_size=10, max_overflow=20)
AsyncSessionLocal = async_sessionmaker(bind=async_engine)


async def create_database():
    async with async_engine.begin() as connect:
        await connect.run_sync(Base.metadata.create_all)
        await connect.commit()


async def drop_database():
    async with async_engine.begin() as connect:
        await connect.run_sync(Base.metadata.drop_all)
        await connect.commit()


async def get_session():
    async with AsyncSessionLocal() as session:
        yield session
