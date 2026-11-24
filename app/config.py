"""Configuración leída de variables de entorno (las define docker-compose.yml)."""

import os

DB_PATH = os.getenv("DB_PATH", "data/smarthome.db")
SMTP_HOST = os.getenv("SMTP_HOST", "localhost")
SMTP_PORT = int(os.getenv("SMTP_PORT", "1025"))
CORREO_REMITENTE = os.getenv("CORREO_REMITENTE", "smarthome@proyecto.local")
