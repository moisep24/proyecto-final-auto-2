"""Une las etapas del motor:
lexer -> parser -> tabla de símbolos -> validador -> IR -> optimizador -> VM.

RESPONSABLE: Pascual. Mientras una etapa no esté implementada, el pipeline
se detiene ahí y lo reporta como "pendiente" en lugar de romperse.
"""

from app.errores import ErrorCompilacion
from app.ir import generador
from app.lenguaje import ast, lexer, parser
from app.optimizador import optimizador
from app.semantica import validador
from app.semantica.tabla_simbolos import TablaSimbolos
from app.vm.maquina import MaquinaVirtual, Servicios


def procesar(codigo: str, dispositivos: list[dict], servicios: Servicios, ejecutar: bool = True) -> dict:
    salida: dict = {
        "tokens": [],
        "ast": None,
        "ir": [],
        "ir_optimizado": [],
        "optimizaciones": [],
        "resultados": [],
        "errores": [],
        "dispositivos_finales": None,  # lista de dispositivos si la VM terminó bien
        "etapa_alcanzada": None,
    }

    def etapa(nombre, funcion):
        salida["etapa_alcanzada"] = nombre
        return funcion()

    try:
        tokens = etapa("lexico", lambda: lexer.analizar(codigo))
        salida["tokens"] = [t.a_dict() for t in tokens]

        programa = etapa("sintactico", lambda: parser.parsear(tokens))
        salida["ast"] = ast.a_dict(programa)

        tabla = etapa("tabla_simbolos", lambda: TablaSimbolos(dispositivos))
        etapa("semantico", lambda: validador.validar(programa, tabla))

        ir = etapa("ir", lambda: generador.generar(programa, tabla))
        salida["ir"] = [str(i) for i in ir]

        ir_opt, cambios = etapa("optimizacion", lambda: optimizador.optimizar(ir))
        salida["ir_optimizado"] = [str(i) for i in ir_opt]
        salida["optimizaciones"] = cambios

        if ejecutar:
            vm = MaquinaVirtual(tabla, servicios)
            salida["resultados"] = etapa("ejecucion", lambda: vm.ejecutar(ir_opt))
            salida["dispositivos_finales"] = tabla.a_lista()
        salida["etapa_alcanzada"] = "fin"

    except NotImplementedError as e:
        salida["errores"].append({"fase": "pendiente", "mensaje": str(e), "linea": None, "columna": None})
    except ErrorCompilacion as e:
        salida["errores"].append(e.a_dict())

    return salida
