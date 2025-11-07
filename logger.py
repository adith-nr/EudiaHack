"""Common logger for FastAPI services."""
import logging

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("llm-service")
