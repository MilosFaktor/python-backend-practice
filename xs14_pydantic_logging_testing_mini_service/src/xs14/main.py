# main.py

from xs14.ingest import read_json_file
from xs14.validate import validate_raw
from xs14.transform import get_active_users
from xs14.output import build_success, build_error
from xs14.logging_setup import setup_logging
from xs14.errors import ErrorInfo
from xs14.utils import get_end_time
from xs14.config import settings

import uuid
import time

logger = setup_logging(__name__, settings.log_level)


def main():
    raw_path = settings.data_ok if settings.mode_data == "ok" else settings.data_bad
    raw = read_json_file(str(raw_path))
    request_id = str(uuid.uuid4())
    start = time.time()
    logger.info(f"Request_id: {request_id} - 'START'")

    logger.info("Ingesting ...")

    if isinstance(raw, ErrorInfo):
        logger.error("Ingest 'ERROR'")
        err = build_error(raw)
        logger.error(err)

        get_end_time(request_id, start, time.time(), logger)

        return

    else:
        logger.info("Ingest 'OK'")

        logger.info("Validating ...")
        data = validate_raw(raw)

        if isinstance(data, ErrorInfo):
            logger.error("Validation 'ERROR'")
            err = build_error(data)
            logger.error(err)

            get_end_time(request_id, start, time.time(), logger)

            return

        else:
            logger.info("Validation 'OK'")

            logger.info("Extracting 'active' users ...")
            data = get_active_users(data)
            logger.info("Extraction 'OK'")

            logger.info("Building output ...")
            data = build_success(data)
            logger.info("Output built successfuly:")
            logger.info(data)

            get_end_time(request_id, start, time.time(), logger)

            return


if __name__ == "__main__":
    main()
