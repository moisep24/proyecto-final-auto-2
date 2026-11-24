"""Errores del lenguaje. CONTRATO compartido por todas las etapas.

Cada etapa lanza su propio tipo de error para que la API pueda decir
en qué fase falló la instrucción (léxica, sintáctica, semántica o de ejecución).
"""


class ErrorCompilacion(Exception):
    """Clase base. `fase` se muestra en la interfaz."""

    fase = "general"

    def __init__(self, mensaje: str, linea: int | None = None, columna: int | None = None):
        super().__init__(mensaje)
        self.mensaje = mensaje
        self.linea = linea
        self.columna = columna

    def a_dict(self) -> dict:
        return {
            "fase": self.fase,
            "mensaje": self.mensaje,
            "linea": self.linea,
            "columna": self.columna,
        }

    def __str__(self) -> str:
        donde = f" (línea {self.linea}, columna {self.columna})" if self.linea else ""
        return f"Error {self.fase}: {self.mensaje}{donde}"


class ErrorLexico(ErrorCompilacion):
    fase = "léxico"


class ErrorSintactico(ErrorCompilacion):
    fase = "sintáctico"


class ErrorSemantico(ErrorCompilacion):
    fase = "semántico"


class ErrorEjecucion(ErrorCompilacion):
    fase = "ejecución"
