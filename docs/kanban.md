# Tarjetas para el Kanban

Copiar cada una como tarjeta en GitHub Projects (columnas: Por hacer, En progreso, En revisión, Terminado).
Las marcadas como Terminado ya están en el repo.

| Tarjeta | Responsable | Columna | Criterio de aceptación |
| --- | --- | --- | --- |
| Estructura del repo y contratos | Pascual | Terminado | `pytest` corre; contratos en `develop` |
| API y persistencia SQLite | Pascual | Terminado | `test_api.py` pasa |
| Lexer | Pascual | Terminado | `test_lexer.py` pasa (10 pruebas) |
| Tabla de símbolos | Pascual | Terminado | `test_tabla_de_simbolos` pasa |
| Envío de correo SMTP | Pascual | Terminado | `test_correo.py` pasa; correo visible en Mailpit |
| CI con GitHub Actions | Pascual | Terminado | `pytest` corre en cada PR |
| Docker Compose con Mailpit | Pascual | En revisión | `docker compose up --build` levanta app y Mailpit (lo prueba Carlosprogramacion12) |
| Parser y AST | Marco1120 | Por hacer | `test_parser.py` pasa sin `@pendiente` |
| Documentar gramática, tokens (con autómata) y AST | Marco1120 | Por hacer | `gramatica.md`, `tokens.md`, `ast.md` completos |
| Validador semántico | JonathanRene | Por hacer | `test_semantica.py` pasa |
| Generador de IR | JonathanRene | Por hacer | `test_ir.py` pasa |
| Documentar semántica e IR | JonathanRene | Por hacer | `semantica.md`, `ir.md` completos |
| Máquina virtual | Uriel-tech302 | Por hacer | `test_vm.py` pasa |
| Dos optimizaciones | Uriel-tech302 | Por hacer | `test_optimizador.py` pasa, incluida la de equivalencia |
| Documentar optimizaciones y ejecutor | Uriel-tech302 | Por hacer | `optimizaciones.md`, `ejecutor.md` completos |
| Probar Docker Compose | Carlosprogramacion12 | Por hacer | la app abre en :8000 y Mailpit en :8025 |
| Historial, notificaciones y ejemplos en la interfaz | Carlosprogramacion12 | Por hacer | se ven al ejecutar comandos |
| AST como árbol y optimizaciones en la interfaz | Carlosprogramacion12 | Por hacer | se muestran las etapas de forma legible |
| Documentar interfaz | Carlosprogramacion12 | Por hacer | `interfaz.md` con capturas |
| Integración final | Todos | Por hacer | `test_escenarios.py` pasa sin `@integracion` |
| Presentación y demo | Todos | Por hacer | demo de los 13 escenarios obligatorios |
