from decimal import Decimal
from datetime import datetime, timezone

from enum import Enum
from sqlmodel import Field, SQLModel, create_engine
from sqlalchemy import ForeignKey, Column, Numeric

from engine import engine

engine = engine


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None


# crear las tablas (busca clases que heredan SQLModel)
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_db_and_tables()