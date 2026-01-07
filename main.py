from engine import engine, get_session
from fastapi import FastAPI, Response, status, Depends, HTTPException
from fastapi.responses import FileResponse
import json
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from models_database import Hero
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from fastapi.middleware.cors import CORSMiddleware
from models_database import create_db_and_tables

engine = engine

tags_metadata = [
    {
        "name": "heroes",
        "description": "heroes"
    }
]

origins = [
    "https://proyecto-prueba-implementar-db-fastapi.onrender.com",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
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
    allow_origins=origins, # Autorizar URL de Render
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="public"), name="static")


@app.get("/")
async def read_index():
    return FileResponse("public/index.html")

@app.post("/heroes", response_model=Hero, tags=['heroes'])
async def create_hero(hero: Hero, session: AsyncSession = Depends(get_session)):
    try:
        session.add(hero)
        await session.commit()
        await session.refresh(hero)
        return hero
    except Exception: # Capturar error de duplicado
        await session.rollback() # Cancelar la operación
        raise HTTPException(status_code=400, detail="El nombre del héroe ya existe")
    
# Evento de inicio para crear tablas
@app.on_event("startup")
async def on_startup():
    await create_db_and_tables()