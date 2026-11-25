# Cómo trabajar en el repo

## Reglas

1. **Nadie sube cambios directo a `main` ni a `develop`.** Todo entra por Pull Request.
2. Cada PR lo revisa y aprueba **otro integrante** antes de hacer merge.
3. **Los contratos no se cambian sin avisar en el grupo:**
   `tokens.py`, `ast.py`, `instrucciones.py`, `dispositivos.py`, `errores.py`.
   Si necesitas cambiar uno, avisa primero, porque afecta el trabajo de los demás.
4. Antes de abrir un PR, `pytest` debe pasar en tu computadora.
5. Cada quien documenta su parte en `docs/`.

## Primera vez

```bash
git clone https://github.com/<usuario>/proyecto-final-auto-2.git
cd proyecto-final-auto-2
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest                              # debe terminar sin "failed"
git checkout feature/<tu-modulo>    # ver la tabla de abajo
```

## Ramas por integrante

| Integrante | Rama(s) | Archivos | Pruebas |
| --- | --- | --- | --- |
| Pascual (líder) | `feature/api`, `feature/docker` | `app/api`, `app/db`, `app/pipeline.py`, Docker | `test_api.py`, `test_escenarios.py` |
| Marco1120 · Lenguaje | `feature/lexer`, `feature/parser` | `app/lenguaje/lexer.py`, `parser.py` | `test_lexer.py`, `test_parser.py` |
| JonathanRene · Semántico e IR | `feature/semantic`, `feature/ir` | `app/semantica/`, `app/ir/generador.py` | `test_semantica.py`, `test_ir.py` |
| Uriel-tech302 · Optimización y VM | `feature/optimizer`, `feature/executor` | `app/optimizador/`, `app/vm/` | `test_optimizador.py`, `test_vm.py` |
| Por confirmar · Frontend | `feature/frontend` | `app/static/` | prueba manual en el navegador |

Cada módulo tiene, al inicio del archivo, la explicación de qué debe hacer, qué recibe y qué devuelve.
Las pruebas de tu módulo ya están escritas: tu trabajo es hacer que pasen.

## Ciclo de trabajo diario

```bash
git checkout feature/lexer          # tu rama
git pull origin develop             # trae lo nuevo de los demás
# ... programas ...
pytest tests/test_lexer.py          # tus pruebas
git add app/lenguaje/lexer.py tests/test_lexer.py
git commit -m "feat(lexer): reconocer cadenas entre comillas"
git push origin feature/lexer
```

Cuando una parte funcione, abre un **Pull Request** en GitHub de tu rama hacia `develop`.

## Cuando termines tu módulo

1. En tus archivos de prueba, borra la línea `@pendiente` de encima de cada prueba.
2. Corre `pytest`: tus pruebas deben salir como `passed`.
3. Abre el PR y pide revisión.

## Formato de commits

```
tipo(módulo): descripción en presente
```

| Tipo | Uso |
| --- | --- |
| `feat` | funcionalidad nueva |
| `fix` | corrección de un error |
| `test` | pruebas |
| `docs` | documentación |
| `refactor` | reorganizar código sin cambiar lo que hace |

Ejemplos: `feat(parser): soportar SI ... ENTONCES`, `fix(vm): salto a etiqueta inexistente`,
`docs(ir): tabla de instrucciones intermedias`.

## Kanban (GitHub Projects)

Columnas: **Por hacer → En progreso → En revisión → Terminado**.
Cada tarjeta lleva responsable, criterios de aceptación y el enlace a su PR.
Mueve tu tarjeta cuando cambie de estado.
