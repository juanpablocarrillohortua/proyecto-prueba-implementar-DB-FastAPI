from engine import engine, get_session
from fastapi import FastAPI, Response, status, Depends
import json
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from models_database import Hero
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

engine = engine

tags_metadata = [
    {
        "name": "heroes",
        "description": "heroes"
    }
]


app = FastAPI(title='Heroes API',
              description="ApiRestFul para la gestión de vehiculos",
              version="0.0.2",
              contact={
                  "name": "Juan Pablo Carrillo Hortua",
                  "url": "https://github.com/juanpablocarrillohortua"
              },
              license_info={
                  "name": "Apache 2.0",
                  "url": "https://www.apache.org/licenses/LICENSE-2.0.html"
              },
              openapi_tags=tags_metadata)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # En producción, pon aquí la URL de tu web
    allow_credentials=True,
    allow_methods=["*"], # Permite todos los métodos (POST, GET, etc.)
    allow_headers=["*"], # Permite todos los encabezados
)

app.mount("/static", StaticFiles(directory="public"), name="static")


@app.post("/heroes/", response_model=Hero, tags=['heroes'])
async def create_hero(hero: Hero, session: AsyncSession = Depends(get_session)):
    # SQLModel permite añadir el objeto directamente
    session.add(hero)
    await session.commit()
    await session.refresh(hero)
    return hero