# Tokens reconocidos

> Responsable: Integrante 2. Definidos en `app/lenguaje/tokens.py`.

| Token | Patrón | Ejemplo |
| --- | --- | --- |
| Palabras reservadas (ENCENDER, APAGAR, ACTIVAR, DESACTIVAR, ABRIR, CERRAR, CONSULTAR, LISTAR, NOTIFICAR, ENVIAR, DISPOSITIVOS, CORREO, A, MENSAJE, SI, ENTONCES) | la palabra, sin importar mayúsculas | `ENCENDER` |
| ESTADO | ENCENDIDO, APAGADO, ACTIVADA, DESACTIVADA, ABIERTA, CERRADA | `ENCENDIDO` |
| IDENTIFICADOR | `[A-Za-z_][A-Za-z0-9_]*` que no sea reservada | `luz_sala` |
| CADENA | `"` cualquier texto sin salto de línea `"` | `"Hola"` |
| IGUAL / DIFERENTE | `==` / `!=` | `==` |
| SALTO_LINEA | `\n` | |
| FIN | fin de la entrada | |

## Autómata

_Dibujar el AFD del lexer (estados para identificador, cadena, operador) y explicarlo._

## Errores léxicos

| Entrada | Error |
| --- | --- |
| `ENCENDER luz_sala@` | Carácter '@' no reconocido (línea 1, columna 18) |
| `NOTIFICAR "hola` | Cadena sin cerrar |
