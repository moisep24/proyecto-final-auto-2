"""Persistencia en SQLite.  RESPONSABLE: Integrante 1

Tablas (ver docs/modelo_datos.md):
  dispositivos(id, tipo, estado)
  historial(id, fecha, codigo, exito, salida_json)
  notificaciones(id, fecha, mensaje)
"""

import json
import os
import sqlite3
from contextlib import contextmanager
from datetime import datetime

from app import config
from app.semantica.dispositivos import DISPOSITIVOS_INICIALES, operaciones_permitidas

ESQUEMA = """
CREATE TABLE IF NOT EXISTS dispositivos (
    id      TEXT PRIMARY KEY,
    tipo    TEXT NOT NULL,
    estado  TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS historial (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha        TEXT NOT NULL,
    codigo       TEXT NOT NULL,
    exito        INTEGER NOT NULL,
    salida_json  TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS notificaciones (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha    TEXT NOT NULL,
    mensaje  TEXT NOT NULL
);
"""


def _ahora() -> str:
    return datetime.now().isoformat(timespec="seconds")


@contextmanager
def conexion():
    carpeta = os.path.dirname(config.DB_PATH)
    if carpeta:
        os.makedirs(carpeta, exist_ok=True)
    con = sqlite3.connect(config.DB_PATH)
    con.row_factory = sqlite3.Row
    try:
        yield con
        con.commit()
    finally:
        con.close()


def inicializar(reiniciar: bool = False) -> None:
    with conexion() as con:
        if reiniciar:
            con.executescript(
                "DROP TABLE IF EXISTS dispositivos; DROP TABLE IF EXISTS historial; "
                "DROP TABLE IF EXISTS notificaciones;"
            )
        con.executescript(ESQUEMA)
        if con.execute("SELECT COUNT(*) FROM dispositivos").fetchone()[0] == 0:
            con.executemany(
                "INSERT INTO dispositivos (id, tipo, estado) VALUES (:id, :tipo, :estado)",
                DISPOSITIVOS_INICIALES,
            )


def obtener_dispositivos() -> list[dict]:
    with conexion() as con:
        filas = con.execute("SELECT id, tipo, estado FROM dispositivos ORDER BY rowid").fetchall()
    return [
        {**dict(f), "operaciones": sorted(operaciones_permitidas(f["tipo"]))}
        for f in filas
    ]


def guardar_estados(dispositivos: list[dict]) -> None:
    with conexion() as con:
        con.executemany(
            "UPDATE dispositivos SET estado = :estado WHERE id = :id",
            [{"id": d["id"], "estado": d["estado"]} for d in dispositivos],
        )


def guardar_historial(codigo: str, exito: bool, salida: dict) -> None:
    with conexion() as con:
        con.execute(
            "INSERT INTO historial (fecha, codigo, exito, salida_json) VALUES (?, ?, ?, ?)",
            (_ahora(), codigo, int(exito), json.dumps(salida, ensure_ascii=False)),
        )


def obtener_historial(limite: int = 50) -> list[dict]:
    with conexion() as con:
        filas = con.execute(
            "SELECT id, fecha, codigo, exito, salida_json FROM historial ORDER BY id DESC LIMIT ?",
            (limite,),
        ).fetchall()
    return [
        {
            "id": f["id"],
            "fecha": f["fecha"],
            "codigo": f["codigo"],
            "exito": bool(f["exito"]),
            "errores": json.loads(f["salida_json"]).get("errores", []),
        }
        for f in filas
    ]


def agregar_notificacion(mensaje: str) -> None:
    with conexion() as con:
        con.execute("INSERT INTO notificaciones (fecha, mensaje) VALUES (?, ?)", (_ahora(), mensaje))


def obtener_notificaciones(limite: int = 50) -> list[dict]:
    with conexion() as con:
        filas = con.execute(
            "SELECT id, fecha, mensaje FROM notificaciones ORDER BY id DESC LIMIT ?", (limite,)
        ).fetchall()
    return [dict(f) for f in filas]
