import logging
import os

logger = logging.getLogger("demo")
logger.setLevel(os.getenv("LOG_LEVEL", "INFO"))
print(logger.name)
logger.info("request_received")

logger.info("ddb_write_success")
logger.info("idempotency_hit")
logger.warning("validation_failed")
