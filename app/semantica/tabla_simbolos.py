"""Tabla de símbolos.  IMPLEMENTADA (Pascual). La usa JonathanRene en el validador y el IR.

Registra los dispositivos disponibles: identificador, tipo, estado actual
y operaciones permitidas. La construye la API con lo que hay en la base
de datos y la usan el validador semántico, el generador de IR y la máquina virtual.

    tabla = TablaSimbolos([{"id": "luz_sala", "tipo": "LED", "estado": "APAGADO"}, ...])
    tabla.existe("luz_sala")                 -> True
    tabla.tipo("luz_sala")                   -> "LED"
    tabla.estado("luz_sala")                 -> "APAGADO"
    tabla.operaciones("luz_sala")            -> {"ENCENDER", "APAGAR", "CONSULTAR"}
    tabla.estados_validos("luz_sala")        -> ["ENCENDIDO", "APAGADO"]
    tabla.estado_resultante("luz_sala", "ENCENDER") -> "ENCENDIDO"
    tabla.actualizar_estado("luz_sala", "ENCENDIDO")
    tabla.a_lista()   -> [{"id", "tipo", "estado", "operaciones"}, ...]  (para la API y LISTAR)
"""

from dataclasses import dataclass

from app.semantica.dispositivos import TIPOS, operaciones_permitidas


@dataclass
class Simbolo:
    id: str
    tipo: str
    estado: str


class TablaSimbolos:
    def __init__(self, dispositivos: list[dict]):
        self._simbolos: dict[str, Simbolo] = {}
        for d in dispositivos:
            if d["tipo"] not in TIPOS:
                raise ValueError(f"Tipo de dispositivo desconocido: {d['tipo']}")
            self._simbolos[d["id"]] = Simbolo(d["id"], d["tipo"], d["estado"])

    def _obtener(self, ident: str) -> Simbolo:
        if ident not in self._simbolos:
            raise KeyError(f"El dispositivo '{ident}' no existe")
        return self._simbolos[ident]

    def existe(self, ident: str) -> bool:
        return ident in self._simbolos

    def tipo(self, ident: str) -> str:
        return self._obtener(ident).tipo

    def estado(self, ident: str) -> str:
        return self._obtener(ident).estado

    def operaciones(self, ident: str) -> set[str]:
        return operaciones_permitidas(self.tipo(ident))

    def estados_validos(self, ident: str) -> list[str]:
        return list(TIPOS[self.tipo(ident)]["estados"])

    def estado_resultante(self, ident: str, operacion: str) -> str:
        return TIPOS[self.tipo(ident)]["operaciones"][operacion]

    def actualizar_estado(self, ident: str, estado: str) -> None:
        self._obtener(ident).estado = estado

    def a_lista(self) -> list[dict]:
        return [
            {"id": s.id, "tipo": s.tipo, "estado": s.estado, "operaciones": sorted(self.operaciones(s.id))}
            for s in self._simbolos.values()
        ]
