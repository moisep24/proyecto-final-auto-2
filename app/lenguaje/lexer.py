"""Analizador léxico.  IMPLEMENTADO (Pascual). Revisión y documentación: Marco1120

Entrada:  el código fuente como texto (una o varias líneas).
Salida:   lista de Token, terminada SIEMPRE con un Token FIN.
Errores:  ErrorLexico con línea y columna.

Funciona como un autómata finito determinista que se recorre carácter por carácter.
Según el primer carácter de cada lexema, entra a un estado distinto:

    estado inicial
      ├─ espacio / tabulador  -> se ignora
      ├─ '#'                  -> comentario hasta el fin de línea (se ignora)
      ├─ salto de línea       -> SALTO_LINEA (se omiten repetidos y al inicio)
      ├─ letra o '_'          -> IDENT: consume [A-Za-z0-9_]*
      │                          y luego clasifica: palabra reservada, ESTADO o IDENTIFICADOR
      ├─ '"'                  -> CADENA: consume hasta la siguiente '"' (sin cruzar línea)
      ├─ '=' seguido de '='   -> IGUAL
      ├─ '!' seguido de '='   -> DIFERENTE
      └─ cualquier otro       -> ErrorLexico("Carácter 'x' no reconocido")

Las palabras reservadas y los estados no distinguen mayúsculas ("encender" == "ENCENDER");
los identificadores se guardan tal como se escribieron.
"""

from app.errores import ErrorLexico
from app.lenguaje.tokens import PALABRAS_RESERVADAS, VALORES_ESTADO, TipoToken, Token


def _es_inicio_ident(c: str) -> bool:
    return c.isascii() and (c.isalpha() or c == "_")


def _es_parte_ident(c: str) -> bool:
    return c.isascii() and (c.isalnum() or c == "_")


def analizar(codigo: str) -> list[Token]:
    tokens: list[Token] = []
    i = 0
    linea, columna = 1, 1
    n = len(codigo)

    def agregar_salto():
        # No se generan saltos al inicio ni repetidos: las líneas vacías no cuentan.
        if tokens and tokens[-1].tipo != TipoToken.SALTO_LINEA:
            tokens.append(Token(TipoToken.SALTO_LINEA, "\\n", linea, columna))

    while i < n:
        c = codigo[i]

        if c == "\n":
            agregar_salto()
            i += 1
            linea += 1
            columna = 1
            continue

        if c in " \t\r":
            i += 1
            columna += 1
            continue

        if c == "#":
            while i < n and codigo[i] != "\n":
                i += 1
            continue

        if _es_inicio_ident(c):
            inicio, col_inicio = i, columna
            while i < n and _es_parte_ident(codigo[i]):
                i += 1
            lexema = codigo[inicio:i]
            columna += i - inicio
            mayus = lexema.upper()
            if mayus in PALABRAS_RESERVADAS:
                tokens.append(Token(PALABRAS_RESERVADAS[mayus], mayus, linea, col_inicio))
            elif mayus in VALORES_ESTADO:
                tokens.append(Token(TipoToken.ESTADO, mayus, linea, col_inicio))
            else:
                tokens.append(Token(TipoToken.IDENTIFICADOR, lexema, linea, col_inicio))
            continue

        if c == '"':
            col_inicio = columna
            fin = i + 1
            while fin < n and codigo[fin] not in '"\n':
                fin += 1
            if fin >= n or codigo[fin] == "\n":
                raise ErrorLexico("Cadena sin cerrar: falta la comilla final", linea, col_inicio)
            tokens.append(Token(TipoToken.CADENA, codigo[i + 1:fin], linea, col_inicio))
            columna += fin - i + 1
            i = fin + 1
            continue

        dos = codigo[i:i + 2]
        if dos in ("==", "!="):
            tipo = TipoToken.IGUAL if dos == "==" else TipoToken.DIFERENTE
            tokens.append(Token(tipo, dos, linea, columna))
            i += 2
            columna += 2
            continue

        raise ErrorLexico(f"Carácter '{c}' no reconocido", linea, columna)

    # Quitar un salto final para que el parser no vea "instrucción vacía".
    if tokens and tokens[-1].tipo == TipoToken.SALTO_LINEA:
        tokens.pop()
    tokens.append(Token(TipoToken.FIN, "", linea, columna))
    return tokens
