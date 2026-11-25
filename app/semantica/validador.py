"""Análisis semántico.  RESPONSABLE: JonathanRene   RAMA: feature/semantic

Recorre el AST y verifica que cada instrucción tenga sentido. No modifica nada.

Validaciones mínimas (documentarlas en docs/semantica.md):
  1. El dispositivo existe:            ENCENDER dispositivo99 -> "El dispositivo 'dispositivo99' no existe"
  2. La operación es compatible:       ENCENDER alarma1       -> "La operación ENCENDER no es válida para alarma1 (ALARMA)"
  3. En SI, el estado comparado es de ese tipo:
                                       SI alarma1 == ENCENDIDO -> "alarma1 (ALARMA) no puede estar ENCENDIDO"
  4. ENVIAR CORREO: el destinatario tiene formato de correo y el mensaje no está vacío.
  5. NOTIFICAR: el mensaje no está vacío.

Lanza ErrorSemantico(mensaje, linea) en el primer error que encuentre.
"""

from app.errores import ErrorSemantico  # noqa: F401
from app.lenguaje import ast
from app.semantica.tabla_simbolos import TablaSimbolos


def validar(programa: ast.Programa, tabla: TablaSimbolos) -> None:
    raise NotImplementedError("Validador semántico pendiente (JonathanRene)")
