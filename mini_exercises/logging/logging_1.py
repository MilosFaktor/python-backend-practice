import logging
<<<<<<< HEAD


"""
    setting logger with 2 handlers
    each handler has set different logging level 
    i_handler -> main.log
    e_handler -> error.log

    """
logger = logging.getLogger(__name__)
logger.setLevel("INFO")  # can be expressed by value 20 instead


info_handler = logging.FileHandler("main.log", mode="w")
info_handler.setLevel("INFO")
formater = logging.Formatter("%(asctime)s - %(name)s -  %(levelname)s - %(message)s")
info_handler.setFormatter(formater)

error_handler = logging.FileHandler("error.log", mode="w")
error_handler.setLevel("ERROR")  # can be expressed by value 40 instead
error_handler.setFormatter(formater)

logger.addHandler(info_handler)
logger.addHandler(error_handler)


logger.info("testing custom logger")
logger.error("testing error")
=======
import uuid

logging.basicConfig(
    level=logging.INFO,
    filename="loging_1.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s)",
)

r_id = str(uuid.uuid4())

logging.debug(f"[request_id]: {r_id} - this is a debug message")
logging.info(f"[request_id]: {r_id} - this is an info message")
logging.warning(f"[request_id]: {r_id} - this is a warning message")
logging.error(f"[request_id]: {r_id} - this is an error message")
logging.critical(f"[request_id]: {r_id} - this is a critical message")


try:
    x = 1 / 0
except ZeroDivisionError as e:
    logging.exception("ZeroDivisionError")
>>>>>>> xs14
