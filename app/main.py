"""Punto de entrada.  uvicorn app.main:app --reload"""

from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.api.rutas import router
from app.db import database

ESTATICOS = Path(__file__).parent / "static"


@asynccontextmanager
async def ciclo_de_vida(app: FastAPI):
    database.inicializar()
    yield


app = FastAPI(title="SmartHome – Proyecto final Autómatas II", lifespan=ciclo_de_vida)
app.include_router(router)
app.mount("/static", StaticFiles(directory=ESTATICOS), name="static")


@app.get("/", include_in_schema=False)
def inicio():
    return FileResponse(ESTATICOS / "index.html")
