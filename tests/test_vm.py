"""Pruebas de la máquina virtual (Integrante 4). Usa TablaFalsa y ServiciosFalsos
para no depender de otros módulos ni de Mailpit."""

import pytest

from app.errores import ErrorEjecucion
from app.ir.instrucciones import InstrIR, OpIR
from app.vm.maquina import MaquinaVirtual
from tests.conftest import pendiente


def I(op, *args):  # noqa: E743
    return InstrIR(op, args)


@pendiente
def test_set_state(tabla_falsa, servicios_falsos):
    MaquinaVirtual(tabla_falsa, servicios_falsos).ejecutar([I(OpIR.SET_STATE, "luz_sala", "ENCENDIDO"), I(OpIR.HALT)])
    assert tabla_falsa.estado("luz_sala") == "ENCENDIDO"


@pendiente
def test_get_state_produce_resultado(tabla_falsa, servicios_falsos):
    res = MaquinaVirtual(tabla_falsa, servicios_falsos).ejecutar([I(OpIR.GET_STATE, "alarma1"), I(OpIR.HALT)])
    assert "DESACTIVADA" in res[0]["mensaje"]


@pendiente
def test_condicional_falso_salta(tabla_falsa, servicios_falsos):
    ir = [
        I(OpIR.COMPARE, "luz_sala", "==", "ENCENDIDO"),  # luz_sala empieza APAGADO
        I(OpIR.JUMP_IF_FALSE, "L1"),
        I(OpIR.SET_STATE, "alarma1", "ACTIVADA"),
        I(OpIR.LABEL, "L1"),
        I(OpIR.HALT),
    ]
    MaquinaVirtual(tabla_falsa, servicios_falsos).ejecutar(ir)
    assert tabla_falsa.estado("alarma1") == "DESACTIVADA"


@pendiente
def test_condicional_verdadero_ejecuta(tabla_falsa, servicios_falsos):
    ir = [
        I(OpIR.COMPARE, "luz_sala", "==", "APAGADO"),
        I(OpIR.JUMP_IF_FALSE, "L1"),
        I(OpIR.SET_STATE, "alarma1", "ACTIVADA"),
        I(OpIR.LABEL, "L1"),
        I(OpIR.HALT),
    ]
    MaquinaVirtual(tabla_falsa, servicios_falsos).ejecutar(ir)
    assert tabla_falsa.estado("alarma1") == "ACTIVADA"


@pendiente
def test_notificar_y_correo(tabla_falsa, servicios_falsos):
    MaquinaVirtual(tabla_falsa, servicios_falsos).ejecutar(
        [I(OpIR.NOTIFY, "Prueba"), I(OpIR.SEND_EMAIL, "a@b.com", "Hola"), I(OpIR.HALT)]
    )
    assert servicios_falsos.notificaciones == ["Prueba"]
    assert servicios_falsos.correos == [("a@b.com", "Hola")]


@pendiente
def test_estado_invalido(tabla_falsa, servicios_falsos):
    with pytest.raises(ErrorEjecucion):
        MaquinaVirtual(tabla_falsa, servicios_falsos).ejecutar([I(OpIR.SET_STATE, "luz_sala", "ACTIVADA")])
