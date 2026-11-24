"""Endpoints REST.  RESPONSABLE: Integrante 1

POST /api/ejecutar        {"codigo": "...", "ejecutar": true}
GET  /api/dispositivos
GET  /api/historial
GET  /api/notificaciones
POST /api/reiniciar       regresa los dispositivos a su estado inicial
"""

from fastapi import APIRouter
from pydantic import BaseModel

from app import pipeline
from app.db import database
from app.vm import correo


class ServiciosReales:
    """Implementación de los servicios que usa la VM."""

    def notificar(self, mensaje: str) -> None:
        database.agregar_notificacion(mensaje)

    def enviar_correo(self, destinatario: str, mensaje: str) -> None:
        correo.enviar_correo(destinatario, mensaje)


class PeticionEjecutar(BaseModel):
    codigo: str
    ejecutar: bool = True  # False = solo analizar (útil para ver tokens, AST e IR)


router = APIRouter(prefix="/api")


@router.post("/ejecutar")
def ejecutar(peticion: PeticionEjecutar) -> dict:
    salida = pipeline.procesar(
        peticion.codigo,
        database.obtener_dispositivos(),
        ServiciosReales(),
        ejecutar=peticion.ejecutar,
    )
    if salida["dispositivos_finales"] is not None:
        database.guardar_estados(salida["dispositivos_finales"])
    exito = not salida["errores"]
    if peticion.ejecutar:
        database.guardar_historial(peticion.codigo, exito, salida)
    salida.pop("dispositivos_finales")
    salida["exito"] = exito
    salida["dispositivos"] = database.obtener_dispositivos()
    return salida


@router.get("/dispositivos")
def dispositivos() -> list[dict]:
    return database.obtener_dispositivos()


@router.get("/historial")
def historial() -> list[dict]:
    return database.obtener_historial()


@router.get("/notificaciones")
def notificaciones() -> list[dict]:
    return database.obtener_notificaciones()


@router.post("/reiniciar")
def reiniciar() -> dict:
    database.inicializar(reiniciar=True)
    return {"ok": True}
