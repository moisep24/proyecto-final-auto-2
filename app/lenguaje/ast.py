"""Nodos del Árbol Sintáctico Abstracto (AST). CONTRATO.

El parser (Marco1120) construye estos nodos; el analizador semántico (JonathanRene)
y el generador de IR (JonathanRene) los recorren.
"""

from dataclasses import dataclass, field, fields, is_dataclass


@dataclass
class Nodo:
    linea: int = field(default=0, kw_only=True)


@dataclass
class Comando(Nodo):
    """ENCENDER | APAGAR | ACTIVAR | DESACTIVAR | ABRIR | CERRAR <dispositivo>"""

    operacion: str  # "ENCENDER", "APAGAR", ...
    dispositivo: str


@dataclass
class Consultar(Nodo):
    """CONSULTAR <dispositivo>"""

    dispositivo: str


@dataclass
class Listar(Nodo):
    """LISTAR DISPOSITIVOS"""


@dataclass
class Notificar(Nodo):
    """NOTIFICAR "mensaje" """

    mensaje: str


@dataclass
class EnviarCorreo(Nodo):
    """ENVIAR CORREO A "destinatario" MENSAJE "texto" """

    destinatario: str
    mensaje: str


@dataclass
class Comparacion(Nodo):
    """<dispositivo> (== | !=) <ESTADO>"""

    dispositivo: str
    operador: str  # "==" o "!="
    valor: str     # "ENCENDIDO", "ACTIVADA", ...


@dataclass
class Condicional(Nodo):
    """SI <comparacion> ENTONCES <instruccion>"""

    condicion: Comparacion
    entonces: Nodo


@dataclass
class Programa(Nodo):
    instrucciones: list[Nodo]


def a_dict(nodo) -> dict | list | str | int | None:
    """Convierte el AST en un diccionario JSON para mostrarlo en la interfaz."""
    if isinstance(nodo, list):
        return [a_dict(n) for n in nodo]
    if is_dataclass(nodo):
        datos = {"nodo": type(nodo).__name__}
        for f in fields(nodo):
            datos[f.name] = a_dict(getattr(nodo, f.name))
        return datos
    return nodo
