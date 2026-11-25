"""Máquina virtual que ejecuta el IR.  RESPONSABLE: Uriel-tech302   RAMA: feature/executor

Recorre la lista de InstrIR con un contador de programa (pc) y un registro `flag`.

Para cada instrucción:
  SET_STATE d E      -> valida que E sea un estado válido de d, llama
                        tabla.actualizar_estado(d, E) y agrega un resultado
  GET_STATE d        -> agrega {"tipo": "consulta", "mensaje": "luz_sala está ENCENDIDO"}
  COMPARE d op E     -> flag = (tabla.estado(d) == E)   (o != según op)
  JUMP_IF_FALSE L    -> si not flag: pc = posición de LABEL L
  LABEL L            -> no hace nada
  LIST               -> agrega {"tipo": "lista", "mensaje": ..., "datos": tabla.a_lista()}
  NOTIFY msg         -> servicios.notificar(msg) y agrega un resultado
  SEND_EMAIL d m     -> servicios.enviar_correo(d, m) y agrega un resultado
  HALT               -> termina

Cada resultado es un dict: {"tipo": "...", "mensaje": "...", "linea": n}.
Errores en tiempo de ejecución (por ejemplo, falla el SMTP) -> ErrorEjecucion.
"""

from typing import Protocol

from app.errores import ErrorEjecucion  # noqa: F401
from app.ir.instrucciones import InstrIR, OpIR  # noqa: F401
from app.semantica.tabla_simbolos import TablaSimbolos


class Servicios(Protocol):
    """Lo que la VM puede pedir al exterior. La API le pasa la implementación real."""

    def notificar(self, mensaje: str) -> None: ...

    def enviar_correo(self, destinatario: str, mensaje: str) -> None: ...


class MaquinaVirtual:
    def __init__(self, tabla: TablaSimbolos, servicios: Servicios):
        self.tabla = tabla
        self.servicios = servicios

    def ejecutar(self, ir: list[InstrIR]) -> list[dict]:
        raise NotImplementedError("Máquina virtual pendiente (Uriel-tech302)")
