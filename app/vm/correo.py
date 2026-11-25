"""Envío de correo por SMTP a Mailpit.  IMPLEMENTADO (Pascual). Lo usa la VM de Uriel-tech302.

Mailpit corre en Docker y acepta cualquier correo sin autenticación:
  - SMTP en  SMTP_HOST:SMTP_PORT  (mailpit:1025 dentro de Docker, localhost:1025 fuera)
  - Bandeja web en http://localhost:8025 para ver los correos recibidos
"""

import smtplib
from email.message import EmailMessage

from app import config
from app.errores import ErrorEjecucion


def enviar_correo(destinatario: str, mensaje: str) -> None:
    msg = EmailMessage()
    msg["From"] = config.CORREO_REMITENTE
    msg["To"] = destinatario
    msg["Subject"] = "Notificación de SmartHome"
    msg.set_content(mensaje)
    try:
        with smtplib.SMTP(config.SMTP_HOST, config.SMTP_PORT, timeout=5) as servidor:
            servidor.send_message(msg)
    except (OSError, smtplib.SMTPException) as e:
        raise ErrorEjecucion(
            f"No se pudo enviar el correo a {destinatario}: servidor SMTP "
            f"{config.SMTP_HOST}:{config.SMTP_PORT} no disponible ({e.__class__.__name__})"
        ) from e
