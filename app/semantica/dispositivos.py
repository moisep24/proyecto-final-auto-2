"""Catálogo de tipos de dispositivo y dispositivos iniciales. CONTRATO.

La tabla de símbolos (Int. 3) se construye a partir de esto y de lo que
hay guardado en la base de datos.
"""

# Para cada tipo: qué operación lleva a qué estado, y qué estados son válidos.
TIPOS: dict[str, dict] = {
    "LED": {
        "operaciones": {"ENCENDER": "ENCENDIDO", "APAGAR": "APAGADO"},
        "estados": ["ENCENDIDO", "APAGADO"],
    },
    "VENTILADOR": {
        "operaciones": {"ENCENDER": "ENCENDIDO", "APAGAR": "APAGADO"},
        "estados": ["ENCENDIDO", "APAGADO"],
    },
    "ALARMA": {
        "operaciones": {"ACTIVAR": "ACTIVADA", "DESACTIVAR": "DESACTIVADA"},
        "estados": ["ACTIVADA", "DESACTIVADA"],
    },
    "PUERTA": {
        "operaciones": {"ABRIR": "ABIERTA", "CERRAR": "CERRADA"},
        "estados": ["ABIERTA", "CERRADA"],
    },
}

# CONSULTAR se permite en todos los tipos.
OPERACIONES_COMUNES = {"CONSULTAR"}

DISPOSITIVOS_INICIALES: list[dict] = [
    {"id": "luz_sala", "tipo": "LED", "estado": "APAGADO"},
    {"id": "luz_cocina", "tipo": "LED", "estado": "APAGADO"},
    {"id": "ventilador1", "tipo": "VENTILADOR", "estado": "APAGADO"},
    {"id": "alarma1", "tipo": "ALARMA", "estado": "DESACTIVADA"},
    {"id": "puerta_principal", "tipo": "PUERTA", "estado": "CERRADA"},
]


def operaciones_permitidas(tipo: str) -> set[str]:
    return set(TIPOS[tipo]["operaciones"]) | OPERACIONES_COMUNES
