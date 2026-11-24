"""Analizador léxico.  RESPONSABLE: Integrante 2   RAMA: feature/lexer

Entrada:  el código fuente como texto (una o varias líneas).
Salida:   lista de Token, terminada SIEMPRE con un Token FIN.
Errores:  ErrorLexico con línea y columna.

Reglas que hay que reconocer (ver docs/tokens.md):
  - Palabras reservadas (PALABRAS_RESERVADAS), sin importar mayúsculas: "encender" == "ENCENDER".
  - Valores de estado (VALORES_ESTADO) -> TipoToken.ESTADO
  - Identificadores: letra o _ seguida de letras, dígitos o _  -> IDENTIFICADOR (se respeta el texto)
  - Cadenas entre comillas dobles -> CADENA (el lexema va SIN comillas). Cadena sin cerrar = error.
  - Operadores == y !=
  - Saltos de línea -> SALTO_LINEA (las líneas vacías se pueden ignorar)
  - Espacios y tabuladores se ignoran
  - Cualquier otro carácter -> ErrorLexico("Carácter '@' no reconocido", linea, columna)

Ejemplo:
    analizar("ENCENDER luz_sala")
    -> [Token(ENCENDER, "ENCENDER", 1, 1), Token(IDENTIFICADOR, "luz_sala", 1, 10), Token(FIN, "", 1, 18)]
"""

from app.errores import ErrorLexico  # noqa: F401
from app.lenguaje.tokens import PALABRAS_RESERVADAS, VALORES_ESTADO, TipoToken, Token  # noqa: F401


def analizar(codigo: str) -> list[Token]:
    raise NotImplementedError("Lexer pendiente (Integrante 2)")
