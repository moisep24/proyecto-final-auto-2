"""Pruebas del envío de correo (Pascual). No necesitan Mailpit: se simula el servidor."""

import pytest

from app import config
from app.errores import ErrorEjecucion
from app.vm import correo


class SMTPFalso:
    enviados = []

    def __init__(self, host, port, timeout=None):
        self.host, self.port = host, port

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False

    def send_message(self, msg):
        SMTPFalso.enviados.append(msg)


def test_envia_mensaje(monkeypatch):
    monkeypatch.setattr(correo.smtplib, "SMTP", SMTPFalso)
    correo.enviar_correo("admin@casa.com", "Hola")
    msg = SMTPFalso.enviados[-1]
    assert msg["To"] == "admin@casa.com"
    assert msg.get_content().strip() == "Hola"


def test_servidor_caido_da_error_de_ejecucion(monkeypatch):
    monkeypatch.setattr(config, "SMTP_HOST", "127.0.0.1")
    monkeypatch.setattr(config, "SMTP_PORT", 1)  # puerto cerrado
    with pytest.raises(ErrorEjecucion):
        correo.enviar_correo("admin@casa.com", "Hola")
