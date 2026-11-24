# Arquitectura

> Responsable: Integrante 1

## Flujo de una instrucción

```
Navegador ──POST /api/ejecutar──▶ API FastAPI ──▶ pipeline.procesar()
                                                    │
   lexer ──tokens──▶ parser ──AST──▶ validador ◀── tabla de símbolos (desde SQLite)
                                       │
                         generador IR ──IR──▶ optimizador ──IR'──▶ máquina virtual
                                                                    │        │
                                                              SQLite (estados)  Mailpit (SMTP)
```

Cada etapa lanza su propio tipo de error (`ErrorLexico`, `ErrorSintactico`, `ErrorSemantico`,
`ErrorEjecucion`), así la interfaz indica en qué fase falló la instrucción.

## Separación lenguaje / ejecución

El procesamiento del lenguaje (lexer, parser, semántico, IR, optimizador) no conoce
la base de datos ni el correo. La máquina virtual recibe la tabla de símbolos y un objeto
`Servicios` (notificar, enviar_correo) que la API implementa. Para agregar un comando nuevo:
token → regla de la gramática → nodo del AST → validación → instrucción IR → caso en la VM.

## Contrato de la API

| Método | Ruta | Descripción |
| --- | --- | --- |
| POST | `/api/ejecutar` | `{"codigo": "...", "ejecutar": true}` → tokens, ast, ir, ir_optimizado, optimizaciones, resultados, errores, dispositivos, exito |
| GET | `/api/dispositivos` | dispositivos con estado y operaciones permitidas |
| GET | `/api/historial` | últimas 50 ejecuciones |
| GET | `/api/notificaciones` | notificaciones registradas |
| POST | `/api/reiniciar` | regresa los dispositivos al estado inicial |

## Despliegue

`docker compose up --build` levanta dos servicios:

- `app`: FastAPI + motor + SQLite (puerto 8000). La base de datos vive en un volumen.
- `mailpit`: servidor SMTP de pruebas (1025) con bandeja web (8025).

## Tecnologías

Python 3.12, FastAPI, SQLite, HTML/CSS/JavaScript, Pytest, Docker Compose, Mailpit,
GitHub + GitHub Projects + GitHub Actions (corre `pytest` en cada PR).
