"""Pruebas del optimizador (Uriel-tech302). Incluye la prueba obligatoria de que
las optimizaciones conservan el resultado."""

import pytest

from app.ir.instrucciones import InstrIR, OpIR
from app.optimizador.optimizador import optimizar
from app.vm.maquina import MaquinaVirtual
from tests.conftest import ServiciosFalsos, TablaFalsa, pendiente

SET, GET, NOTIFY, CMP, JIF, LABEL, HALT = (
    OpIR.SET_STATE, OpIR.GET_STATE, OpIR.NOTIFY, OpIR.COMPARE, OpIR.JUMP_IF_FALSE, OpIR.LABEL, OpIR.HALT,
)


def I(op, *args):  # noqa: E743
    return InstrIR(op, args)


def opt(*ir):
    resultado, _ = optimizar(list(ir))
    return [str(i) for i in resultado]


@pendiente
def test_elimina_redundante():
    assert opt(I(SET, "luz_sala", "ENCENDIDO"), I(SET, "luz_sala", "ENCENDIDO"), I(HALT)) == [
        "SET_STATE luz_sala ENCENDIDO", "HALT",
    ]


@pendiente
def test_elimina_sobrescrita():
    assert opt(I(SET, "luz_sala", "ENCENDIDO"), I(SET, "luz_sala", "APAGADO"), I(HALT)) == [
        "SET_STATE luz_sala APAGADO", "HALT",
    ]


@pendiente
def test_no_elimina_si_hay_lectura_en_medio():
    ir = [I(SET, "luz_sala", "ENCENDIDO"), I(GET, "luz_sala"), I(SET, "luz_sala", "APAGADO"), I(HALT)]
    assert opt(*ir) == [str(i) for i in ir]


@pendiente
def test_no_toca_efectos_externos():
    ir = [I(SET, "luz_sala", "ENCENDIDO"), I(NOTIFY, "hola"), I(SET, "luz_sala", "APAGADO"), I(NOTIFY, "hola"), I(HALT)]
    assert opt(*ir) == [str(i) for i in ir]


@pendiente
def test_no_cruza_etiquetas():
    ir = [
        I(SET, "luz_sala", "ENCENDIDO"),
        I(CMP, "alarma1", "==", "ACTIVADA"),
        I(JIF, "L1"),
        I(SET, "luz_sala", "APAGADO"),
        I(LABEL, "L1"),
        I(HALT),
    ]
    assert opt(*ir) == [str(i) for i in ir]


@pendiente
def test_reporta_cambios():
    _, cambios = optimizar([I(SET, "luz_sala", "ENCENDIDO"), I(SET, "luz_sala", "ENCENDIDO"), I(HALT)])
    assert len(cambios) == 1


CASOS_EQUIVALENCIA = [
    [I(SET, "luz_sala", "ENCENDIDO"), I(SET, "luz_sala", "ENCENDIDO"), I(HALT)],
    [I(SET, "luz_sala", "ENCENDIDO"), I(SET, "luz_sala", "APAGADO"), I(SET, "alarma1", "ACTIVADA"), I(HALT)],
    [I(SET, "ventilador1", "ENCENDIDO"), I(CMP, "ventilador1", "==", "ENCENDIDO"), I(JIF, "L1"),
     I(SET, "luz_sala", "ENCENDIDO"), I(SET, "luz_sala", "ENCENDIDO"), I(LABEL, "L1"), I(HALT)],
]


@pendiente
@pytest.mark.parametrize("ir", CASOS_EQUIVALENCIA)
def test_optimizacion_conserva_el_resultado(ir):
    """Ejecuta el IR original y el optimizado y compara estados y efectos."""
    t1, s1 = TablaFalsa(), ServiciosFalsos()
    MaquinaVirtual(t1, s1).ejecutar(ir)
    t2, s2 = TablaFalsa(), ServiciosFalsos()
    MaquinaVirtual(t2, s2).ejecutar(optimizar(ir)[0])
    assert t1.estados() == t2.estados()
    assert s1.notificaciones == s2.notificaciones and s1.correos == s2.correos
