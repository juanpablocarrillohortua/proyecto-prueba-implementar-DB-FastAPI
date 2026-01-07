from decimal import Decimal
from datetime import datetime, timezone
import asyncio
from enum import Enum
from sqlmodel import Field, SQLModel, create_engine
from sqlalchemy import ForeignKey, Column, Numeric
from sqlalchemy.ext.asyncio import AsyncEngine

from engine import engine

engine = engine


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None


# crear las tablas (busca clases que heredan SQLModel)
async def create_db_and_tables():
    # Correr como asincrona una accion sincrona
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

