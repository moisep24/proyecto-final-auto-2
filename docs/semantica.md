# Análisis semántico

> Responsable: JonathanRene

## Tabla de símbolos

| Identificador | Tipo | Estado inicial | Operaciones permitidas |
| --- | --- | --- | --- |
| luz_sala | LED | APAGADO | ENCENDER, APAGAR, CONSULTAR |
| luz_cocina | LED | APAGADO | ENCENDER, APAGAR, CONSULTAR |
| ventilador1 | VENTILADOR | APAGADO | ENCENDER, APAGAR, CONSULTAR |
| alarma1 | ALARMA | DESACTIVADA | ACTIVAR, DESACTIVAR, CONSULTAR |
| puerta_principal | PUERTA | CERRADA | ABRIR, CERRAR, CONSULTAR |

_Explicar cómo se construye (desde la base de datos) y qué métodos ofrece._

## Validaciones

| # | Regla | Ejemplo que falla | Mensaje |
| --- | --- | --- | --- |
| 1 | El dispositivo existe | `ENCENDER dispositivo99` | |
| 2 | La operación es compatible con el tipo | `ENCENDER alarma1` | |
| 3 | El estado comparado pertenece al tipo | `SI alarma1 == ENCENDIDO ...` | |
| 4 | El destinatario es un correo válido | `ENVIAR CORREO A "x" ...` | |
| 5 | El mensaje no está vacío | `NOTIFICAR ""` | |

## Acciones semánticas

_Ejemplo: `ENCENDER luz_sala` → verificarDispositivo, verificarOperacion, construirInstruccion._
