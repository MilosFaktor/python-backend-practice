# logging_setup.py

import logging
from typing import Literal
from pathlib import Path


def setup_logging(
    name: str,
    level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO",
) -> logging.Logger:
    values = {"DEBUG": 10, "INFO": 20, "WARNING": 30, "ERROR": 40, "CRITICAL": 50}

    if not level in values:
        raise ValueError(
            "incorrect value! must be = Literal['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']"
        )

    log_dir = Path("logs")
    if not log_dir.exists():
        log_dir.mkdir()

    logger = logging.getLogger(name)
    logger.setLevel(values[level])

    if not logger.handlers:
        handler = logging.FileHandler(f"logs/xs14.log", mode="w")
        handler.setLevel(values[level])

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
