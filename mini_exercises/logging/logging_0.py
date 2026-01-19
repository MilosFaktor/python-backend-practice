import logging

logging.basicConfig(
    level=logging.INFO,
    filename="log.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

handler = logging.FileHandler("test.log")
formater = logging.Formatter("%(asctime)s - %(name)s -  %(levelname)s - %(message)s")
handler.setFormatter(formater)

logger.addHandler(handler)

logger.info("testing custom logger")
