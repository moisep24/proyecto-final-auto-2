"""Generador de código intermedio.  RESPONSABLE: JonathanRene   RAMA: feature/ir

Entrada: Programa ya validado + TablaSimbolos (para saber a qué estado lleva cada operación).
Salida:  lista de InstrIR que SIEMPRE termina con HALT.

Traducción (ver app/ir/instrucciones.py y docs/ir.md):
    ENCENDER luz_sala          -> SET_STATE luz_sala ENCENDIDO
    ACTIVAR alarma1            -> SET_STATE alarma1 ACTIVADA
    CONSULTAR luz_sala         -> GET_STATE luz_sala
    LISTAR DISPOSITIVOS        -> LIST
    NOTIFICAR "hola"           -> NOTIFY "hola"
    ENVIAR CORREO A "a@b.c" MENSAJE "x" -> SEND_EMAIL "a@b.c" "x"
    SI x == E ENTONCES instr   -> COMPARE x == E
                                  JUMP_IF_FALSE L<n>
                                  <instr traducida>
                                  LABEL L<n>
Usa un contador para que cada condicional tenga su propia etiqueta (L1, L2, ...).
Guarda en cada InstrIR la `linea` del nodo que la generó.
"""

from app.ir.instrucciones import InstrIR, OpIR  # noqa: F401
from app.lenguaje import ast
from app.semantica.tabla_simbolos import TablaSimbolos


def generar(programa: ast.Programa, tabla: TablaSimbolos) -> list[InstrIR]:
    raise NotImplementedError("Generador de IR pendiente (JonathanRene)")
