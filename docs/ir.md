# Representación intermedia

> Responsable: Integrante 3. Definida en `app/ir/instrucciones.py`.

| Instrucción | Significado |
| --- | --- |
| `SET_STATE disp ESTADO` | cambia el estado (asignación idempotente) |
| `GET_STATE disp` | lee el estado y lo agrega a la salida |
| `COMPARE disp OP ESTADO` | flag ← estado(disp) OP ESTADO |
| `JUMP_IF_FALSE L` | si flag es falso, salta a `LABEL L` |
| `LABEL L` | destino de salto |
| `LIST` | lista los dispositivos |
| `NOTIFY "msg"` | registra una notificación (efecto externo) |
| `SEND_EMAIL "dest" "msg"` | envía un correo (efecto externo) |
| `HALT` | termina |

## Traducción

| Fuente | IR |
| --- | --- |
| `ENCENDER luz_sala` | `SET_STATE luz_sala ENCENDIDO` |
| `CONSULTAR alarma1` | `GET_STATE alarma1` |
| `SI luz_sala == ENCENDIDO ENTONCES APAGAR luz_sala` | `COMPARE luz_sala == ENCENDIDO` / `JUMP_IF_FALSE L1` / `SET_STATE luz_sala APAGADO` / `LABEL L1` |

_Explicar el recorrido del AST y el contador de etiquetas._
