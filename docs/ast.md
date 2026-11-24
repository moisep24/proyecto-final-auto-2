# Diseño del AST

> Responsable: Integrante 2. Nodos definidos en `app/lenguaje/ast.py`.

| Nodo | Campos | Instrucción |
| --- | --- | --- |
| Programa | instrucciones | todo el código |
| Comando | operacion, dispositivo | ENCENDER luz_sala |
| Consultar | dispositivo | CONSULTAR luz_sala |
| Listar | — | LISTAR DISPOSITIVOS |
| Notificar | mensaje | NOTIFICAR "x" |
| EnviarCorreo | destinatario, mensaje | ENVIAR CORREO A "a@b.c" MENSAJE "x" |
| Condicional | condicion, entonces | SI ... ENTONCES ... |
| Comparacion | dispositivo, operador, valor | luz_sala == ENCENDIDO |

## Ejemplo

`SI luz_sala == ENCENDIDO ENTONCES APAGAR luz_sala`

```
Programa
└── Condicional
    ├── condicion: Comparacion(luz_sala, ==, ENCENDIDO)
    └── entonces:  Comando(APAGAR, luz_sala)
```

_Agregar captura de la vista del AST en la interfaz._
