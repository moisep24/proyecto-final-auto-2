"""Pruebas de la tabla de símbolos y el validador (JonathanRene).
El AST se arma a mano para no depender del parser."""

import pytest

from app.errores import ErrorSemantico
from app.lenguaje import ast
from app.semantica.dispositivos import DISPOSITIVOS_INICIALES
from app.semantica.tabla_simbolos import TablaSimbolos
from app.semantica.validador import validar
from tests.conftest import pendiente


def tabla():
    return TablaSimbolos([dict(d) for d in DISPOSITIVOS_INICIALES])


def prog(*instrucciones):
    return ast.Programa(list(instrucciones))


def test_tabla_de_simbolos():
    t = tabla()
    assert t.existe("luz_sala") and not t.existe("dispositivo99")
    assert t.tipo("alarma1") == "ALARMA"
    assert "ENCENDER" in t.operaciones("luz_sala")
    assert t.estado_resultante("alarma1", "ACTIVAR") == "ACTIVADA"
    t.actualizar_estado("luz_sala", "ENCENDIDO")
    assert t.estado("luz_sala") == "ENCENDIDO"


@pendiente
def test_programa_valido_no_lanza_error():
    validar(prog(ast.Comando("ENCENDER", "luz_sala", linea=1)), tabla())


@pendiente
def test_dispositivo_inexistente():
    with pytest.raises(ErrorSemantico):
        validar(prog(ast.Comando("ENCENDER", "dispositivo99", linea=1)), tabla())


@pendiente
def test_operacion_incompatible():
    with pytest.raises(ErrorSemantico):
        validar(prog(ast.Comando("ENCENDER", "alarma1", linea=1)), tabla())


@pendiente
def test_condicional_con_estado_de_otro_tipo():
    cond = ast.Condicional(ast.Comparacion("alarma1", "==", "ENCENDIDO"), ast.Notificar("x"))
    with pytest.raises(ErrorSemantico):
        validar(prog(cond), tabla())


@pendiente
def test_correo_invalido():
    with pytest.raises(ErrorSemantico):
        validar(prog(ast.EnviarCorreo("no-es-correo", "hola")), tabla())
