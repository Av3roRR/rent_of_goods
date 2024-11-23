from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from app.config import settings

async_engine = create_async_engine(url=settings.DATABASE_URL)

async_session_maker = async_sessionmaker(async_engine, expire_on_commit=False)



class Base(DeclarativeBase):
    pass
