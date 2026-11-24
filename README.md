# SmartHome · Proyecto final Lenguajes y Autómatas II

Aplicación web que simula una casa inteligente controlada por instrucciones escritas.
Cada instrucción pasa por un compilador completo: análisis léxico, sintáctico y
semántico, código intermedio, optimización y ejecución en una máquina virtual.

```
ENCENDER luz_sala
ACTIVAR alarma1
SI alarma1 == ACTIVADA ENTONCES NOTIFICAR "Alarma activada"
ENVIAR CORREO A "admin@casa.com" MENSAJE "Todo en orden"
```

Instituto Tecnológico de Oaxaca · Ingeniería en Sistemas Computacionales.

## Equipo

| Integrante | Rol | Módulos |
| --- | --- | --- |
| Pascual Coyolt Moisés | Líder técnico y backend | `app/api`, `app/db`, `app/pipeline.py`, Docker |
| _Integrante 2_ | Lenguaje | `app/lenguaje/lexer.py`, `app/lenguaje/parser.py` |
| _Integrante 3_ | Semántico e IR | `app/semantica/`, `app/ir/generador.py` |
| _Integrante 4_ | Optimización y ejecución | `app/optimizador/`, `app/vm/` |
| _Integrante 5_ | Frontend | `app/static/` |

## Cómo ejecutarlo

### Con Docker (forma oficial de entrega)

```bash
docker compose up --build
```

- Aplicación: http://localhost:8000
- Bandeja de correos de prueba (Mailpit): http://localhost:8025
- Documentación de la API: http://localhost:8000/docs

### Sin Docker (para desarrollar)

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Para probar el correo sin Docker, levanta solo Mailpit: `docker compose up mailpit`.

### Pruebas

```bash
pytest
```

Las pruebas marcadas como `xfail` son de módulos que aún no se implementan.
Cada integrante quita el `@pendiente` de sus pruebas cuando termina su módulo.

## Lenguaje

| Instrucción | Ejemplo | Dispositivos |
| --- | --- | --- |
| ENCENDER / APAGAR | `ENCENDER luz_sala` | LED, VENTILADOR |
| ACTIVAR / DESACTIVAR | `ACTIVAR alarma1` | ALARMA |
| ABRIR / CERRAR | `ABRIR puerta_principal` | PUERTA |
| CONSULTAR | `CONSULTAR ventilador1` | todos |
| LISTAR | `LISTAR DISPOSITIVOS` | — |
| NOTIFICAR | `NOTIFICAR "Hola"` | — |
| ENVIAR CORREO | `ENVIAR CORREO A "a@b.com" MENSAJE "Hola"` | — |
| SI … ENTONCES | `SI luz_sala == ENCENDIDO ENTONCES APAGAR luz_sala` | — |

Dispositivos iniciales: `luz_sala`, `luz_cocina`, `ventilador1`, `alarma1`, `puerta_principal`.

## Estructura

```
app/
├── errores.py          # CONTRATO: tipos de error por fase
├── pipeline.py         # une todas las etapas
├── lenguaje/
│   ├── tokens.py       # CONTRATO: tipos de token
│   ├── ast.py          # CONTRATO: nodos del AST
│   ├── lexer.py        # Integrante 2
│   └── parser.py       # Integrante 2
├── semantica/
│   ├── dispositivos.py # CONTRATO: tipos y dispositivos
│   ├── tabla_simbolos.py  # Integrante 3
│   └── validador.py       # Integrante 3
├── ir/
│   ├── instrucciones.py   # CONTRATO: instrucciones intermedias
│   └── generador.py       # Integrante 3
├── optimizador/optimizador.py  # Integrante 4
├── vm/maquina.py, correo.py    # Integrante 4
├── api/rutas.py, db/database.py  # Integrante 1
└── static/                       # Integrante 5
tests/                  # una prueba por módulo + escenarios obligatorios
docs/                   # documentación técnica, una sección por integrante
```

## Documentación técnica

Ver la carpeta [`docs/`](docs/). Para colaborar, lee [`CONTRIBUTING.md`](CONTRIBUTING.md).
