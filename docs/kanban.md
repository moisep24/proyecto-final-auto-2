# Tarjetas para el Kanban

Copiar cada una como tarjeta en GitHub Projects (columnas: Por hacer, En progreso, En revisión, Terminado).

| Tarjeta | Responsable | Criterio de aceptación |
| --- | --- | --- |
| Estructura del repo y contratos | Int. 1 | `pytest` corre; contratos en `develop` |
| API y persistencia SQLite | Int. 1 | `test_api.py` pasa |
| Docker Compose con Mailpit | Int. 1 | `docker compose up --build` levanta app y Mailpit |
| Lexer | Int. 2 | `test_lexer.py` pasa sin `@pendiente` |
| Parser y AST | Int. 2 | `test_parser.py` pasa sin `@pendiente` |
| Documentar gramática, tokens y AST | Int. 2 | `gramatica.md`, `tokens.md`, `ast.md` completos |
| Tabla de símbolos | Int. 3 | `test_tabla_de_simbolos` pasa |
| Validador semántico | Int. 3 | `test_semantica.py` pasa |
| Generador de IR | Int. 3 | `test_ir.py` pasa |
| Documentar semántica e IR | Int. 3 | `semantica.md`, `ir.md` completos |
| Máquina virtual | Int. 4 | `test_vm.py` pasa |
| Envío de correo SMTP | Int. 4 | correo visible en http://localhost:8025 |
| Dos optimizaciones | Int. 4 | `test_optimizador.py` pasa, incluida la de equivalencia |
| Documentar optimizaciones y ejecutor | Int. 4 | `optimizaciones.md`, `ejecutor.md` completos |
| Consola y panel de dispositivos | Int. 5 | se ve el cambio de estado al ejecutar |
| Vista de tokens, AST, IR e historial | Int. 5 | se muestran las 4 etapas y el historial |
| Integración final | Todos | `test_escenarios.py` pasa sin `@integracion` |
| Presentación y demo | Todos | demo de los 13 escenarios obligatorios |
