
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

from app.config import settings

# Create a database engine to connect with database
engine = create_async_engine(
    # database type/dialect and file name
    url=settings.POSTGRES_URL,
    # Log sql queries
    echo=True,
)


async def create_db_tables():
    async with engine.begin() as connection:
        # from app.api.schemas.shipment import Shipment  # type: ignore
        await connection.run_sync(SQLModel.metadata.create_all)


async def get_session():
    async_session = sessionmaker(
        bind=engine, class_=AsyncSession, expire_on_commit=False, # type: ignore
    )

    async with async_session() as session: # type: ignore
        yield session


