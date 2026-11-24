"""Las 13 pruebas funcionales obligatorias (sección 16 del documento), de punta a punta
a través de la API. Se activan solas cuando todas las etapas estén implementadas;
entonces quiten el @integracion."""

import pytest

from tests.conftest import integracion


def ejecutar(cliente, codigo):
    return cliente.post("/api/ejecutar", json={"codigo": codigo}).json()


def estado(r, ident):
    return next(d["estado"] for d in r["dispositivos"] if d["id"] == ident)


@integracion
@pytest.mark.parametrize(
    "codigo, dispositivo, esperado",
    [
        ("ENCENDER luz_sala", "luz_sala", "ENCENDIDO"),
        ("ENCENDER luz_sala\nAPAGAR luz_sala", "luz_sala", "APAGADO"),
        ("ACTIVAR alarma1", "alarma1", "ACTIVADA"),
        ("ACTIVAR alarma1\nDESACTIVAR alarma1", "alarma1", "DESACTIVADA"),
        ("ENCENDER luz_sala\nSI luz_sala == ENCENDIDO ENTONCES APAGAR luz_sala", "luz_sala", "APAGADO"),
    ],
)
def test_cambios_de_estado(cliente, codigo, dispositivo, esperado):
    r = ejecutar(cliente, codigo)
    assert r["exito"], r["errores"]
    assert estado(r, dispositivo) == esperado


@integracion
def test_consultar(cliente):
    r = ejecutar(cliente, "CONSULTAR luz_sala")
    assert r["exito"] and "APAGADO" in r["resultados"][0]["mensaje"]


@integracion
def test_listar(cliente):
    r = ejecutar(cliente, "LISTAR DISPOSITIVOS")
    assert r["exito"] and r["resultados"][0]["tipo"] == "lista"


@integracion
def test_notificar(cliente):
    r = ejecutar(cliente, 'NOTIFICAR "Prueba"')
    assert r["exito"]
    assert cliente.get("/api/notificaciones").json()[0]["mensaje"] == "Prueba"


@integracion
@pytest.mark.parametrize(
    "codigo, fase",
    [
        ("ENCENDER dispositivo99", "semántico"),
        ("ENCENDER alarma1", "semántico"),
        ("ENCENDER", "sintáctico"),
        ("ENCENDER luz_sala@", "léxico"),
    ],
)
def test_errores(cliente, codigo, fase):
    r = ejecutar(cliente, codigo)
    assert not r["exito"]
    assert r["errores"][0]["fase"] == fase


# El escenario de ENVIAR CORREO se demuestra con Mailpit levantado:
#   docker compose up --build  ->  ejecutar el comando  ->  abrir http://localhost:8025
