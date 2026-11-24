"""Pruebas del parser (Integrante 2). Quita @pendiente cuando lo implementes."""

import pytest

from app.errores import ErrorSintactico
from app.lenguaje import ast
from app.lenguaje.lexer import analizar
from app.lenguaje.parser import parsear
from tests.conftest import pendiente


def p(codigo):
    return parsear(analizar(codigo))


@pendiente
def test_comando_de_control():
    prog = p("APAGAR luz_sala")
    assert prog.instrucciones == [ast.Comando("APAGAR", "luz_sala", linea=1)]


@pendiente
def test_listar_y_consultar():
    prog = p("LISTAR DISPOSITIVOS\nCONSULTAR alarma1")
    assert isinstance(prog.instrucciones[0], ast.Listar)
    assert prog.instrucciones[1] == ast.Consultar("alarma1", linea=2)


@pendiente
def test_enviar_correo():
    prog = p('ENVIAR CORREO A "admin@casa.com" MENSAJE "Hola"')
    assert prog.instrucciones[0] == ast.EnviarCorreo("admin@casa.com", "Hola", linea=1)


@pendiente
def test_condicional():
    prog = p("SI luz_sala == ENCENDIDO ENTONCES APAGAR luz_sala")
    c = prog.instrucciones[0]
    assert isinstance(c, ast.Condicional)
    assert c.condicion.dispositivo == "luz_sala"
    assert c.condicion.valor == "ENCENDIDO"
    assert c.entonces.operacion == "APAGAR"


@pendiente
def test_error_falta_identificador():
    with pytest.raises(ErrorSintactico):
        p("ENCENDER")


@pendiente
def test_error_listar_sin_dispositivos():
    with pytest.raises(ErrorSintactico):
        p("LISTAR")
