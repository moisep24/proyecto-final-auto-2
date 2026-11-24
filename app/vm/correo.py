"""Envío de correo por SMTP a Mailpit.  RESPONSABLE: Integrante 4   RAMA: feature/executor

Mailpit corre en Docker y acepta cualquier correo sin autenticación:
  - SMTP en  SMTP_HOST:SMTP_PORT  (mailpit:1025 dentro de Docker, localhost:1025 fuera)
  - Bandeja web en http://localhost:8025 para ver los correos recibidos

Implementación sugerida con la librería estándar:

    from email.message import EmailMessage
    import smtplib
    msg = EmailMessage()
    msg["From"] = config.CORREO_REMITENTE
    msg["To"] = destinatario
    msg["Subject"] = "SmartHome"
    msg.set_content(mensaje)
    with smtplib.SMTP(config.SMTP_HOST, config.SMTP_PORT, timeout=5) as s:
        s.send_message(msg)

Si falla la conexión, lanzar ErrorEjecucion("No se pudo conectar al servidor de correo").
"""

from app import config  # noqa: F401
from app.errores import ErrorEjecucion  # noqa: F401


def enviar_correo(destinatario: str, mensaje: str) -> None:
    raise NotImplementedError("Envío de correo pendiente (Integrante 4)")
