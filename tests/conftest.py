import os
import tempfile

import pytest

# La base de datos de pruebas va a un archivo temporal, nunca a data/.
os.environ["DB_PATH"] = os.path.join(tempfile.mkdtemp(), "pruebas.db")

from app.semantica.dispositivos import DISPOSITIVOS_INICIALES, TIPOS, operaciones_permitidas  # noqa: E402

# Marca para pruebas de un módulo que todavía lanza NotImplementedError.
# Cuando implementes tu módulo, BORRA el @pendiente de tus pruebas.
pendiente = pytest.mark.xfail(raises=NotImplementedError, reason="módulo pendiente", strict=False)

# Marca para pruebas de punta a punta: se activan cuando todo el pipeline esté listo.
integracion = pytest.mark.xfail(reason="requiere todas las etapas implementadas", strict=False)


class TablaFalsa:
    """Tabla de símbolos de mentira para probar la VM y el optimizador
    sin depender del módulo del Integrante 3."""

    def __init__(self, dispositivos=None):
        self._d = {d["id"]: dict(d) for d in (dispositivos or DISPOSITIVOS_INICIALES)}

    def existe(self, ident):
        return ident in self._d

    def tipo(self, ident):
        return self._d[ident]["tipo"]

    def estado(self, ident):
        return self._d[ident]["estado"]

    def operaciones(self, ident):
        return operaciones_permitidas(self.tipo(ident))

    def estados_validos(self, ident):
        return TIPOS[self.tipo(ident)]["estados"]

    def estado_resultante(self, ident, operacion):
        return TIPOS[self.tipo(ident)]["operaciones"][operacion]

    def actualizar_estado(self, ident, estado):
        self._d[ident]["estado"] = estado

    def a_lista(self):
        return [
            {**d, "operaciones": sorted(operaciones_permitidas(d["tipo"]))} for d in self._d.values()
        ]

    def estados(self):
        return {k: v["estado"] for k, v in self._d.items()}


class ServiciosFalsos:
    """Guarda las llamadas en listas en lugar de enviar correos de verdad."""

    def __init__(self):
        self.notificaciones = []
        self.correos = []

    def notificar(self, mensaje):
        self.notificaciones.append(mensaje)

    def enviar_correo(self, destinatario, mensaje):
        self.correos.append((destinatario, mensaje))


@pytest.fixture
def tabla_falsa():
    return TablaFalsa()


@pytest.fixture
def servicios_falsos():
    return ServiciosFalsos()


@pytest.fixture
def cliente():
    from fastapi.testclient import TestClient

    from app.db import database
    from app.main import app

    database.inicializar(reiniciar=True)
    with TestClient(app) as c:
        yield c
