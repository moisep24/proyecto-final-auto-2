"""Pruebas del generador de IR (JonathanRene)."""

from app.ir.generador import generar
from app.lenguaje import ast
from app.semantica.dispositivos import DISPOSITIVOS_INICIALES
from app.semantica.tabla_simbolos import TablaSimbolos
from tests.conftest import pendiente


def ir_de(*instrucciones):
    tabla = TablaSimbolos([dict(d) for d in DISPOSITIVOS_INICIALES])
    return [str(i) for i in generar(ast.Programa(list(instrucciones)), tabla)]


@pendiente
def test_comandos_simples():
    assert ir_de(
        ast.Comando("ENCENDER", "luz_sala"),
        ast.Comando("ACTIVAR", "alarma1"),
        ast.Consultar("luz_sala"),
        ast.Listar(),
    ) == [
        "SET_STATE luz_sala ENCENDIDO",
        "SET_STATE alarma1 ACTIVADA",
        "GET_STATE luz_sala",
        "LIST",
        "HALT",
    ]


@pendiente
def test_condicional():
    cond = ast.Condicional(ast.Comparacion("luz_sala", "==", "ENCENDIDO"), ast.Comando("APAGAR", "luz_sala"))
    assert ir_de(cond) == [
        "COMPARE luz_sala == ENCENDIDO",
        "JUMP_IF_FALSE L1",
        "SET_STATE luz_sala APAGADO",
        "LABEL L1",
        "HALT",
    ]


@pendiente
def test_notificar_y_correo():
    assert ir_de(ast.Notificar("Prueba"), ast.EnviarCorreo("a@b.com", "Hola")) == [
        'NOTIFY "Prueba"',
        'SEND_EMAIL "a@b.com" "Hola"',
        "HALT",
    ]
