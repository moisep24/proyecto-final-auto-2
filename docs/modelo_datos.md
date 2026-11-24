# Modelo de base de datos

> Responsable: Integrante 1. SQLite, archivo en `data/smarthome.db` (volumen en Docker).

| Tabla | Campo | Tipo | Descripción |
| --- | --- | --- | --- |
| dispositivos | id | TEXT PK | identificador (`luz_sala`) |
| | tipo | TEXT | LED, VENTILADOR, ALARMA, PUERTA |
| | estado | TEXT | estado actual |
| historial | id | INTEGER PK | autoincremental |
| | fecha | TEXT | ISO 8601 |
| | codigo | TEXT | instrucciones enviadas |
| | exito | INTEGER | 1 si no hubo errores |
| | salida_json | TEXT | respuesta completa del pipeline |
| notificaciones | id | INTEGER PK | autoincremental |
| | fecha | TEXT | ISO 8601 |
| | mensaje | TEXT | texto de NOTIFICAR |

Los tipos de dispositivo y sus operaciones no se guardan en la base: están en
`app/semantica/dispositivos.py`, porque son parte de las reglas del lenguaje.
