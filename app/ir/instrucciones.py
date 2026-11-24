"""Representación intermedia (IR). CONTRATO.

Código de tres direcciones muy simple. La VM tiene un registro de
comparación (`flag`) y un registro de lectura (`r`).

| Instrucción              | Significado                                         |
|--------------------------|-----------------------------------------------------|
| SET_STATE disp ESTADO    | Cambia el estado del dispositivo (idempotente)      |
| GET_STATE disp           | r <- estado(disp); agrega el resultado a la salida  |
| COMPARE disp OP ESTADO   | flag <- (estado(disp) OP ESTADO)                    |
| JUMP_IF_FALSE etiqueta   | si flag es falso, salta a LABEL etiqueta            |
| LABEL etiqueta           | marca un destino de salto (no hace nada)            |
| LIST                     | agrega la lista de dispositivos a la salida         |
| NOTIFY "mensaje"         | registra una notificación (efecto externo)          |
| SEND_EMAIL "dest" "msg"  | envía un correo por SMTP (efecto externo)           |
| HALT                     | termina la ejecución                                |

Ejemplo: SI luz_sala == ENCENDIDO ENTONCES APAGAR luz_sala

    COMPARE luz_sala == ENCENDIDO
    JUMP_IF_FALSE L1
    SET_STATE luz_sala APAGADO
    LABEL L1
    HALT
"""

from dataclasses import dataclass
from enum import Enum, auto


class OpIR(Enum):
    SET_STATE = auto()
    GET_STATE = auto()
    COMPARE = auto()
    JUMP_IF_FALSE = auto()
    LABEL = auto()
    LIST = auto()
    NOTIFY = auto()
    SEND_EMAIL = auto()
    HALT = auto()


# Instrucciones que el optimizador NO puede eliminar ni reordenar.
EFECTOS_EXTERNOS = {OpIR.NOTIFY, OpIR.SEND_EMAIL}

# Instrucciones que leen estado: cortan las optimizaciones de SET_STATE.
LECTURAS = {OpIR.GET_STATE, OpIR.COMPARE, OpIR.LIST}

# Instrucciones de control de flujo: el optimizador trabaja por bloques entre ellas.
CONTROL = {OpIR.JUMP_IF_FALSE, OpIR.LABEL, OpIR.HALT}


@dataclass(frozen=True)
class InstrIR:
    op: OpIR
    args: tuple = ()
    linea: int = 0  # línea del código fuente que la generó

    def __str__(self) -> str:
        # Los argumentos de texto (mensajes y correos) se imprimen entre comillas.
        if self.op in EFECTOS_EXTERNOS:
            return " ".join([self.op.name] + [f'"{a}"' for a in self.args])
        return " ".join([self.op.name] + [str(a) for a in self.args])

    @property
    def tiene_efecto_externo(self) -> bool:
        return self.op in EFECTOS_EXTERNOS
