"""Pruebas de los contratos compartidos (Pascual). Deben pasar siempre."""

from app.errores import ErrorLexico
from app.ir.instrucciones import InstrIR, OpIR
from app.lenguaje import ast
from app.lenguaje.tokens import PALABRAS_RESERVADAS, TipoToken, Token
from app.semantica.dispositivos import DISPOSITIVOS_INICIALES, TIPOS


def test_instr_ir_se_imprime_legible():
    assert str(InstrIR(OpIR.SET_STATE, ("luz_sala", "ENCENDIDO"))) == "SET_STATE luz_sala ENCENDIDO"
    assert str(InstrIR(OpIR.NOTIFY, ("Hola mundo",))) == 'NOTIFY "Hola mundo"'
    assert InstrIR(OpIR.SEND_EMAIL, ("a@b.com", "x")).tiene_efecto_externo


def test_ast_se_convierte_a_dict():
    prog = ast.Programa([ast.Comando("ENCENDER", "luz_sala", linea=1)])
    d = ast.a_dict(prog)
    assert d["nodo"] == "Programa"
    assert d["instrucciones"][0] == {
        "nodo": "Comando", "linea": 1, "operacion": "ENCENDER", "dispositivo": "luz_sala"
    }


def test_token_a_dict():
    t = Token(TipoToken.ENCENDER, "ENCENDER", 1, 1)
    assert t.a_dict()["tipo"] == "ENCENDER"
    assert PALABRAS_RESERVADAS["SI"] is TipoToken.SI


def test_dispositivos_iniciales_validos():
    assert len(DISPOSITIVOS_INICIALES) >= 3
    for d in DISPOSITIVOS_INICIALES:
        assert d["estado"] in TIPOS[d["tipo"]]["estados"]


def test_error_tiene_fase():
    e = ErrorLexico("Carácter '@' no reconocido", 1, 14)
    assert e.a_dict()["fase"] == "léxico"
