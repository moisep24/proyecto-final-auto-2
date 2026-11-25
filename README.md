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

Instituto Tecnológico de Oaxaca · Ingeniería en Sistemas Computacionales · Entrega: **30 de noviembre de 2026**.

## Estado del proyecto (actualizado 25 nov)

| Etapa | Archivo | Responsable | Estado | Pruebas |
| --- | --- | --- | --- | --- |
| Contratos (tokens, AST, IR, dispositivos, errores) | `app/lenguaje/tokens.py`, `ast.py`, `app/ir/instrucciones.py`, ... | Pascual | ✅ Hecho | `test_contratos.py` 5/5 |
| Lexer | `app/lenguaje/lexer.py` | Pascual | ✅ Hecho | `test_lexer.py` 10/10 |
| **Parser y AST** | `app/lenguaje/parser.py` | **Marco1120** | ⏳ Pendiente | `test_parser.py` 0/6 |
| Tabla de símbolos | `app/semantica/tabla_simbolos.py` | Pascual | ✅ Hecho | `test_tabla_de_simbolos` 1/1 |
| **Validador semántico** | `app/semantica/validador.py` | **JonathanRene** | ⏳ Pendiente | `test_semantica.py` 0/5 |
| **Generador de IR** | `app/ir/generador.py` | **JonathanRene** | ⏳ Pendiente | `test_ir.py` 0/3 |
| **Optimizador** | `app/optimizador/optimizador.py` | **Uriel-tech302** | ⏳ Pendiente | `test_optimizador.py` 0/9 |
| **Máquina virtual** | `app/vm/maquina.py` | **Uriel-tech302** | ⏳ Pendiente | `test_vm.py` 0/6 |
| Correo SMTP (Mailpit) | `app/vm/correo.py` | Pascual | ✅ Hecho y probado con Mailpit | `test_correo.py` 2/2 |
| API REST + SQLite | `app/api/`, `app/db/`, `app/pipeline.py` | Pascual | ✅ Hecho | `test_api.py` 5/5 |
| **Interfaz web** | `app/static/` | **Carlosprogramacion12** | 🟡 Versión básica | prueba manual |
| Docker Compose | `Dockerfile`, `docker-compose.yml` | Pascual / **Carlosprogramacion12** prueba | 🟡 Archivo validado, falta correrlo | `docker compose up --build` |
| CI (GitHub Actions) | `.github/workflows/pruebas.yml` | Pascual | ✅ Hecho | corre `pytest` en cada PR |
| Escenarios obligatorios | `tests/test_escenarios.py` | Todos | ⏳ Se activan al terminar todo | 1/12 + correo en Mailpit |

Para ver el estado real en cualquier momento: `pytest`. Lo que sale como `xfailed` es lo que falta.

## Qué le toca a cada quien

Cada archivo pendiente explica al inicio **qué recibe, qué devuelve y qué errores da**.
Las pruebas ya están escritas: el trabajo es que pasen. Cuando terminen, borren el `@pendiente`
de sus pruebas, corran `pytest` y abran un Pull Request hacia `develop`.

### Marco1120 · Lenguaje (rama `feature/parser`)

- [ ] Implementar `app/lenguaje/parser.py`: parser descendente recursivo con la gramática que viene en el archivo. Debe pasar `pytest tests/test_parser.py`.
- [ ] Mensajes de error sintáctico claros: "Se esperaba un identificador de dispositivo después de ENCENDER".
- [ ] Revisar el lexer (ya hecho) y documentarlo en `docs/tokens.md`, incluido el dibujo del autómata (la descripción está en el encabezado de `lexer.py`).
- [ ] Completar `docs/gramatica.md` y `docs/ast.md`.

### JonathanRene · Semántico e IR (ramas `feature/semantic` y `feature/ir`)

- [ ] Implementar `app/semantica/validador.py`: dispositivo existe, operación compatible, estado válido en `SI`, correo válido, mensaje no vacío. Debe pasar `pytest tests/test_semantica.py`.
- [ ] Implementar `app/ir/generador.py`: AST a instrucciones intermedias, con etiquetas `L1`, `L2`, ... para el `SI`. Debe pasar `pytest tests/test_ir.py`.
- [ ] Usar la tabla de símbolos que ya está hecha (`tabla.existe`, `tabla.operaciones`, `tabla.estado_resultante`, ...).
- [ ] Completar `docs/semantica.md` y `docs/ir.md`.

### Uriel-tech302 · Optimización y ejecución (ramas `feature/optimizer` y `feature/executor`)

- [ ] Implementar `app/vm/maquina.py`: contador de programa, registro `flag`, saltos con etiquetas. Debe pasar `pytest tests/test_vm.py`.
- [ ] Implementar `app/optimizador/optimizador.py`: las dos optimizaciones sin cruzar lecturas, efectos externos ni etiquetas. Debe pasar `pytest tests/test_optimizador.py`, incluida la prueba de que conservan el resultado.
- [ ] Para el correo, la VM solo llama `self.servicios.enviar_correo(destinatario, mensaje)`; el envío SMTP ya está hecho.
- [ ] Completar `docs/optimizaciones.md` (con la justificación de cada optimización) y `docs/ejecutor.md`.

### Carlosprogramacion12 · Interfaz y Docker (rama `feature/frontend`)

- [ ] **Probar `docker compose up --build`** en tu computadora y avisar si algo falla (Pascual no tiene Docker).
- [ ] Panel de historial (`GET /api/historial`) y de notificaciones (`GET /api/notificaciones`).
- [ ] Mostrar el AST como árbol en lugar de JSON, y la lista de optimizaciones aplicadas.
- [ ] Botones con ejemplos (los de `ejemplos/demo.txt`) y un enlace a la bandeja de Mailpit (http://localhost:8025).
- [ ] Completar `docs/interfaz.md` con capturas.

### Pascual · Líder

- [ ] Revisar y aprobar los Pull Requests.
- [ ] Integración: quitar `@integracion` de `tests/test_escenarios.py` cuando todo esté en `develop`.
- [ ] Merge final a `main` y entrega.

### Fechas

| Fecha | Meta |
| --- | --- |
| 27 nov | Cada quien abre su Pull Request con sus pruebas en verde |
| 28 nov | Todo integrado en `develop`; pasan los 13 escenarios; docs completas |
| 29 nov | Ensayo de la demo con `ejemplos/demo.txt` |
| 30 nov | Merge a `main` y entrega |

## Equipo

| Integrante | Rol |
| --- | --- |
| Pascual Coyolt Moisés | Líder técnico y backend |
| [Marco1120](https://github.com/Marco1120) | Lenguaje: lexer, parser, AST |
| [JonathanRene](https://github.com/JonathanRene) | Semántico e IR |
| [Uriel-tech302](https://github.com/Uriel-tech302) | Optimización y ejecución |
| [Carlosprogramacion12](https://github.com/Carlosprogramacion12) | Interfaz web y prueba de Docker |

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

Para probar el correo sin Docker, descarga Mailpit de https://github.com/axllent/mailpit/releases
(el `.zip` de Windows o el `.tar.gz` de Linux/Mac), ejecútalo y deja el servidor corriendo.
Escucha en los mismos puertos (1025 SMTP, 8025 web).

### Pruebas

```bash
pytest                         # todo
pytest tests/test_parser.py    # solo tu módulo
```

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
Las líneas que empiezan con `#` son comentarios.

## Estructura

```
app/
├── errores.py             # contrato: tipos de error por fase
├── pipeline.py            # une todas las etapas                 (Pascual)
├── lenguaje/
│   ├── tokens.py, ast.py  # contratos
│   ├── lexer.py           # ✅                                   (Pascual)
│   └── parser.py          # ⏳                                   (Marco1120)
├── semantica/
│   ├── dispositivos.py    # contrato
│   ├── tabla_simbolos.py  # ✅                                   (Pascual)
│   └── validador.py       # ⏳                                   (JonathanRene)
├── ir/
│   ├── instrucciones.py   # contrato
│   └── generador.py       # ⏳                                   (JonathanRene)
├── optimizador/optimizador.py  # ⏳                              (Uriel-tech302)
├── vm/
│   ├── maquina.py         # ⏳                                   (Uriel-tech302)
│   └── correo.py          # ✅                                   (Pascual)
├── api/, db/              # ✅                                   (Pascual)
└── static/                # 🟡                                   (Carlosprogramacion12)
tests/                     # una prueba por módulo + escenarios obligatorios
docs/                      # documentación técnica, una sección por integrante
```

Para colaborar, lee [`CONTRIBUTING.md`](CONTRIBUTING.md). Documentación técnica en [`docs/`](docs/).
