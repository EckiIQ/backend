from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlmodel import Session, SQLModel

engine = create_engine(
    url="sqlite:///./app.db",
    echo=True,
    connect_args={"check_same_thread": False},
)   

def create_db_tables():
    SQLModel.metadata.create_all(bind=engine)
    print("Database and tables created successfully.")

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

