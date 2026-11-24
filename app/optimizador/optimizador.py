"""Optimizador de IR.  RESPONSABLE: Integrante 4   RAMA: feature/optimizer

Entrada: lista de InstrIR.   Salida: nueva lista de InstrIR (no modificar la original).

Optimización 1. Eliminación de instrucciones redundantes
    SET_STATE luz_sala ENCENDIDO
    SET_STATE luz_sala ENCENDIDO      ->  se elimina la segunda
  Válida porque SET_STATE es una asignación idempotente: aplicarla dos veces
  deja el mismo estado que aplicarla una.

Optimización 2. Eliminación de asignaciones sobrescritas
    SET_STATE luz_sala ENCENDIDO      ->  se elimina
    SET_STATE luz_sala APAGADO
  Válida solo si entre las dos NO hay una lectura del dispositivo (GET_STATE,
  COMPARE, LIST) ni un efecto externo (NOTIFY, SEND_EMAIL), porque esas
  instrucciones podrían observar el estado intermedio.

Reglas que NO se pueden romper (las revisa tests/test_optimizador.py):
  - NOTIFY y SEND_EMAIL nunca se eliminan ni se reordenan.
  - Nunca optimizar a través de LABEL o JUMP_IF_FALSE: trabajar por bloques
    básicos (secuencias sin saltos). Así no se rompe el condicional.
  - Ejecutar el IR original y el optimizado debe dejar los mismos estados finales.

Además devuelve, para mostrar en la interfaz, una lista de qué se eliminó y por qué.
"""

from app.ir.instrucciones import CONTROL, EFECTOS_EXTERNOS, LECTURAS, InstrIR, OpIR  # noqa: F401


def optimizar(ir: list[InstrIR]) -> tuple[list[InstrIR], list[str]]:
    """Devuelve (ir_optimizado, cambios). `cambios` son frases como
    'Línea 2: SET_STATE luz_sala ENCENDIDO eliminada (redundante)'."""
    raise NotImplementedError("Optimizador pendiente (Integrante 4)")
