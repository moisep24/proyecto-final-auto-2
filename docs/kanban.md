# Tarjetas para el Kanban

Copiar cada una como tarjeta en GitHub Projects (columnas: Por hacer, En progreso, En revisión, Terminado).

| Tarjeta | Responsable | Criterio de aceptación |
| --- | --- | --- |
| Estructura del repo y contratos | Pascual | `pytest` corre; contratos en `develop` |
| API y persistencia SQLite | Pascual | `test_api.py` pasa |
| Docker Compose con Mailpit | Pascual | `docker compose up --build` levanta app y Mailpit |
| Lexer | Marco1120 | `test_lexer.py` pasa sin `@pendiente` |
| Parser y AST | Marco1120 | `test_parser.py` pasa sin `@pendiente` |
| Documentar gramática, tokens y AST | Marco1120 | `gramatica.md`, `tokens.md`, `ast.md` completos |
| Tabla de símbolos | JonathanRene | `test_tabla_de_simbolos` pasa |
| Validador semántico | JonathanRene | `test_semantica.py` pasa |
| Generador de IR | JonathanRene | `test_ir.py` pasa |
| Documentar semántica e IR | JonathanRene | `semantica.md`, `ir.md` completos |
| Máquina virtual | Uriel-tech302 | `test_vm.py` pasa |
| Envío de correo SMTP | Uriel-tech302 | correo visible en http://localhost:8025 |
| Dos optimizaciones | Uriel-tech302 | `test_optimizador.py` pasa, incluida la de equivalencia |
| Documentar optimizaciones y ejecutor | Uriel-tech302 | `optimizaciones.md`, `ejecutor.md` completos |
| Consola y panel de dispositivos | Por confirmar | se ve el cambio de estado al ejecutar |
| Vista de tokens, AST, IR e historial | Por confirmar | se muestran las 4 etapas y el historial |
| Integración final | Todos | `test_escenarios.py` pasa sin `@integracion` |
| Presentación y demo | Todos | demo de los 13 escenarios obligatorios |
