import os
import logging


HOST = os.environ.get("HOST", "127.0.0.1")
PORT = os.environ.get("PORT", 8080)

REDIS_HOST = os.environ.get("REDIS_HOST", "127.0.0.1")
REDIS_PORT = os.environ.get("REDIS_PORT", "6379")

LOGGER_LEVEL = logging.DEBUG
