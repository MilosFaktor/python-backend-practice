import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler("separate.log", mode="w")
handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.info("Application started")

print(logger.handlers)
"""
%(asctime)s      → timestamp
%(levelname)s    → INFO / ERROR / DEBUG
%(message)s      → your message
%(name)s         → module name
%(filename)s     → file name
%(lineno)d       → line number
%(funcName)s     → function name
"""
