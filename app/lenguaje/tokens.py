"""Tokens del lenguaje SmartHome. CONTRATO: lo usan el lexer y el parser.

Si agregas un comando nuevo, agrégalo aquí y en docs/tokens.md.
"""

from dataclasses import dataclass
from enum import Enum, auto


class TipoToken(Enum):
    # Comandos
    ENCENDER = auto()
    APAGAR = auto()
    ACTIVAR = auto()
    DESACTIVAR = auto()
    ABRIR = auto()
    CERRAR = auto()
    CONSULTAR = auto()
    LISTAR = auto()
    NOTIFICAR = auto()
    ENVIAR = auto()
    # Palabras auxiliares
    DISPOSITIVOS = auto()
    CORREO = auto()
    A = auto()
    MENSAJE = auto()
    SI = auto()
    ENTONCES = auto()
    # Valores de estado: ENCENDIDO, APAGADO, ACTIVADA, DESACTIVADA, ABIERTA, CERRADA
    ESTADO = auto()
    # Operadores
    IGUAL = auto()      # ==
    DIFERENTE = auto()  # !=
    # Datos
    IDENTIFICADOR = auto()  # luz_sala, alarma1 ...
    CADENA = auto()         # "texto entre comillas"
    # Control
    SALTO_LINEA = auto()
    FIN = auto()


PALABRAS_RESERVADAS: dict[str, TipoToken] = {
    "ENCENDER": TipoToken.ENCENDER,
    "APAGAR": TipoToken.APAGAR,
    "ACTIVAR": TipoToken.ACTIVAR,
    "DESACTIVAR": TipoToken.DESACTIVAR,
    "ABRIR": TipoToken.ABRIR,
    "CERRAR": TipoToken.CERRAR,
    "CONSULTAR": TipoToken.CONSULTAR,
    "LISTAR": TipoToken.LISTAR,
    "NOTIFICAR": TipoToken.NOTIFICAR,
    "ENVIAR": TipoToken.ENVIAR,
    "DISPOSITIVOS": TipoToken.DISPOSITIVOS,
    "CORREO": TipoToken.CORREO,
    "A": TipoToken.A,
    "MENSAJE": TipoToken.MENSAJE,
    "SI": TipoToken.SI,
    "ENTONCES": TipoToken.ENTONCES,
}

VALORES_ESTADO = {"ENCENDIDO", "APAGADO", "ACTIVADA", "DESACTIVADA", "ABIERTA", "CERRADA"}

# Comandos que cambian el estado de un dispositivo: COMANDO identificador
COMANDOS_DE_CONTROL = {
    TipoToken.ENCENDER,
    TipoToken.APAGAR,
    TipoToken.ACTIVAR,
    TipoToken.DESACTIVAR,
    TipoToken.ABRIR,
    TipoToken.CERRAR,
}


@dataclass(frozen=True)
class Token:
    tipo: TipoToken
    lexema: str
    linea: int
    columna: int

    def a_dict(self) -> dict:
        return {
            "tipo": self.tipo.name,
            "lexema": self.lexema,
            "linea": self.linea,
            "columna": self.columna,
        }
