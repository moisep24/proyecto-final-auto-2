# Gramática formal

> Responsable: Integrante 2

## EBNF

```ebnf
programa           = instruccion , { SALTO_LINEA , instruccion } , FIN ;
instruccion        = instruccion_simple | condicional ;
instruccion_simple = control | consultar | listar | notificar | enviar_correo ;
control            = ( "ENCENDER" | "APAGAR" | "ACTIVAR" | "DESACTIVAR" | "ABRIR" | "CERRAR" ) , IDENTIFICADOR ;
consultar          = "CONSULTAR" , IDENTIFICADOR ;
listar             = "LISTAR" , "DISPOSITIVOS" ;
notificar          = "NOTIFICAR" , CADENA ;
enviar_correo      = "ENVIAR" , "CORREO" , "A" , CADENA , "MENSAJE" , CADENA ;
condicional        = "SI" , comparacion , "ENTONCES" , instruccion_simple ;
comparacion        = IDENTIFICADOR , ( "==" | "!=" ) , ESTADO ;
```

## Ejemplos válidos e inválidos

| Entrada | Resultado | Motivo |
| --- | --- | --- |
| `ENCENDER luz_sala` | válida | `control` |
| `ENCENDER` | error sintáctico | falta IDENTIFICADOR |
| `LISTAR` | error sintáctico | falta DISPOSITIVOS |
| _completar…_ | | |

## Cómo la implementación respeta la gramática

_Explicar el parser descendente recursivo: una función por regla, cómo se consume cada
token y qué mensaje de error se da cuando no coincide. Pegar una derivación de ejemplo._
