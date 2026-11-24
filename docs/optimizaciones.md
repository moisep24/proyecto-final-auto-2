# Optimizaciones

> Responsable: Integrante 4

## 1. Eliminación de instrucciones redundantes

```
SET_STATE luz_sala ENCENDIDO        SET_STATE luz_sala ENCENDIDO
SET_STATE luz_sala ENCENDIDO   →
```

**Por qué conserva el comportamiento:** _SET_STATE es idempotente…_

## 2. Eliminación de asignaciones sobrescritas

```
SET_STATE luz_sala ENCENDIDO   →    SET_STATE luz_sala APAGADO
SET_STATE luz_sala APAGADO
```

**Por qué conserva el comportamiento:** _no hay lectura intermedia ni efecto observable…_

## Restricciones

- No se cruzan `GET_STATE`, `COMPARE`, `LIST` (leen el estado intermedio).
- No se eliminan ni reordenan `NOTIFY` ni `SEND_EMAIL`.
- Se trabaja por bloques básicos: nunca a través de `LABEL` o `JUMP_IF_FALSE`.

## Evidencia

`tests/test_optimizador.py::test_optimizacion_conserva_el_resultado` ejecuta el IR original y el
optimizado en la máquina virtual y compara los estados finales. _Pegar la salida de pytest._
