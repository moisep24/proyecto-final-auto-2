"""Tabla de símbolos.  RESPONSABLE: Integrante 3   RAMA: feature/semantic

Registra los dispositivos disponibles: identificador, tipo, estado actual
y operaciones permitidas. La construye la API con lo que hay en la base
de datos y la usan el validador semántico y la máquina virtual.

    tabla = TablaSimbolos([{"id": "luz_sala", "tipo": "LED", "estado": "APAGADO"}, ...])
    tabla.existe("luz_sala")                 -> True
    tabla.tipo("luz_sala")                   -> "LED"
    tabla.estado("luz_sala")                 -> "APAGADO"
    tabla.operaciones("luz_sala")            -> {"ENCENDER", "APAGAR", "CONSULTAR"}
    tabla.estados_validos("luz_sala")        -> ["ENCENDIDO", "APAGADO"]
    tabla.estado_resultante("luz_sala", "ENCENDER") -> "ENCENDIDO"
    tabla.actualizar_estado("luz_sala", "ENCENDIDO")
    tabla.a_lista()   -> [{"id", "tipo", "estado", "operaciones"}, ...]  (para la API y LISTAR)
"""

from app.semantica.dispositivos import TIPOS, operaciones_permitidas  # noqa: F401


class TablaSimbolos:
    def __init__(self, dispositivos: list[dict]):
        raise NotImplementedError("Tabla de símbolos pendiente (Integrante 3)")

    def existe(self, ident: str) -> bool:
        raise NotImplementedError

    def tipo(self, ident: str) -> str:
        raise NotImplementedError

    def estado(self, ident: str) -> str:
        raise NotImplementedError

    def operaciones(self, ident: str) -> set[str]:
        raise NotImplementedError

    def estados_validos(self, ident: str) -> list[str]:
        raise NotImplementedError

    def estado_resultante(self, ident: str, operacion: str) -> str:
        raise NotImplementedError

    def actualizar_estado(self, ident: str, estado: str) -> None:
        raise NotImplementedError

    def a_lista(self) -> list[dict]:
        raise NotImplementedError
