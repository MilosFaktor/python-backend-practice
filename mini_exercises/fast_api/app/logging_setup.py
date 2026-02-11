import logging
import pathlib


def setup_logging(log_level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)

    # Create handlers
    console_handler = logging.StreamHandler()

    # Set levels
    console_handler.setLevel(log_level)

    # Create formatters and add to handlers
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_handler.setFormatter(formatter)

    # Add handlers to logger
    logger.addHandler(console_handler)

    return logger
