"""Pruebas de la API y persistencia (Pascual). Deben pasar desde el inicio."""


def test_lista_dispositivos(cliente):
    r = cliente.get("/api/dispositivos")
    assert r.status_code == 200
    ids = [d["id"] for d in r.json()]
    assert "luz_sala" in ids and "alarma1" in ids


def test_ejecutar_responde_con_el_contrato(cliente):
    r = cliente.post("/api/ejecutar", json={"codigo": "ENCENDER luz_sala"})
    assert r.status_code == 200
    datos = r.json()
    for campo in ["tokens", "ast", "ir", "ir_optimizado", "optimizaciones", "resultados", "errores", "dispositivos", "exito"]:
        assert campo in datos


def test_historial_se_guarda(cliente):
    cliente.post("/api/ejecutar", json={"codigo": "LISTAR DISPOSITIVOS"})
    assert cliente.get("/api/historial").json()[0]["codigo"] == "LISTAR DISPOSITIVOS"


def test_reiniciar(cliente):
    assert cliente.post("/api/reiniciar").json() == {"ok": True}
    estados = {d["id"]: d["estado"] for d in cliente.get("/api/dispositivos").json()}
    assert estados["luz_sala"] == "APAGADO"


def test_pagina_principal(cliente):
    assert "SmartHome" in cliente.get("/").text
