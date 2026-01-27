import logging
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
