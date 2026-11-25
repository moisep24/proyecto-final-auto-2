"""Analizador sintáctico descendente recursivo.  RESPONSABLE: Marco1120   RAMA: feature/parser

Entrada:  lista de Token (salida del lexer).
Salida:   un nodo Programa (ver app/lenguaje/ast.py).
Errores:  ErrorSintactico con la línea y un mensaje claro, por ejemplo
          "Se esperaba un identificador de dispositivo después de ENCENDER".

Gramática (EBNF). Documentarla también en docs/gramatica.md:

    programa      = instruccion , { SALTO_LINEA , instruccion } , FIN ;
    instruccion   = control | consultar | listar | notificar | enviar_correo | condicional ;
    control       = ( ENCENDER | APAGAR | ACTIVAR | DESACTIVAR | ABRIR | CERRAR ) , IDENTIFICADOR ;
    consultar     = CONSULTAR , IDENTIFICADOR ;
    listar        = LISTAR , DISPOSITIVOS ;
    notificar     = NOTIFICAR , CADENA ;
    enviar_correo = ENVIAR , CORREO , A , CADENA , MENSAJE , CADENA ;
    condicional   = SI , comparacion , ENTONCES , instruccion_simple ;
    comparacion   = IDENTIFICADOR , ( "==" | "!=" ) , ESTADO ;
    instruccion_simple = control | consultar | listar | notificar | enviar_correo ;

Sugerencia: una función por regla (_programa, _instruccion, _control, ...)
y dos ayudantes: _actual() y _consumir(tipo_esperado, mensaje_de_error).
"""

from app.errores import ErrorSintactico  # noqa: F401
from app.lenguaje import ast  # noqa: F401
from app.lenguaje.tokens import COMANDOS_DE_CONTROL, TipoToken, Token  # noqa: F401


def parsear(tokens: list[Token]) -> ast.Programa:
    raise NotImplementedError("Parser pendiente (Marco1120)")
