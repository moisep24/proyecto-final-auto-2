"""Pruebas del lexer (Integrante 2). Quita @pendiente cuando lo implementes."""

import pytest

from app.errores import ErrorLexico
from app.lenguaje.lexer import analizar
from app.lenguaje.tokens import TipoToken as T
from tests.conftest import pendiente


def tipos(codigo):
    return [t.tipo for t in analizar(codigo)]


@pendiente
def test_comando_simple():
    toks = analizar("ENCENDER luz_sala")
    assert [t.tipo for t in toks] == [T.ENCENDER, T.IDENTIFICADOR, T.FIN]
    assert toks[1].lexema == "luz_sala"
    assert (toks[1].linea, toks[1].columna) == (1, 10)


@pendiente
def test_no_distingue_mayusculas_en_palabras_reservadas():
    assert tipos("encender luz_sala") == [T.ENCENDER, T.IDENTIFICADOR, T.FIN]


@pendiente
def test_cadena_sin_comillas_en_el_lexema():
    toks = analizar('NOTIFICAR "Prueba"')
    assert toks[1].tipo == T.CADENA
    assert toks[1].lexema == "Prueba"


@pendiente
def test_condicional():
    assert tipos("SI luz_sala == ENCENDIDO ENTONCES APAGAR luz_sala") == [
        T.SI, T.IDENTIFICADOR, T.IGUAL, T.ESTADO, T.ENTONCES, T.APAGAR, T.IDENTIFICADOR, T.FIN,
    ]


@pendiente
def test_varias_lineas():
    toks = analizar("ENCENDER luz_sala\nAPAGAR luz_sala")
    assert T.SALTO_LINEA in [t.tipo for t in toks]
    assert toks[-2].linea == 2


@pendiente
def test_error_lexico_caracter_no_reconocido():
    with pytest.raises(ErrorLexico) as e:
        analizar("ENCENDER luz_sala@")
    assert "@" in e.value.mensaje


@pendiente
def test_error_lexico_cadena_sin_cerrar():
    with pytest.raises(ErrorLexico):
        analizar('NOTIFICAR "hola')
