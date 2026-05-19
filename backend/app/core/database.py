from sqlalchemy.ext.asyncio import (create_async_engine, async_sessionmaker, AsyncSession)
from collections.abc import AsyncGenerator

from sqlalchemy.orm import DeclarativeBase

from app.core.settings import settings

engine = create_async_engine(
    settings.database_url,
    echo=True
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

class Base(DeclarativeBase):
    pass

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session

