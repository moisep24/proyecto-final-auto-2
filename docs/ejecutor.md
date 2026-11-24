# Máquina virtual

> Responsable: Integrante 4

_Explicar: contador de programa, registro flag, tabla de etiquetas, qué hace cada instrucción,
cómo se comunica con la tabla de símbolos y con los servicios (notificaciones y correo),
y qué pasa ante un error en tiempo de ejecución._

## Ejemplo de traza

| pc | Instrucción | flag | Efecto |
| --- | --- | --- | --- |
| 0 | COMPARE luz_sala == ENCENDIDO | | |
| 1 | JUMP_IF_FALSE L1 | | |
| … | | | |

## Correo

Se envía por SMTP a Mailpit (`mailpit:1025` en Docker). Los correos se ven en http://localhost:8025.
