# sandbox.py

from xs14.ingest import read_json_file
from xs14.validate import validate_raw
from xs14.transform import get_active_users
from xs14.output import build_success, build_error

import logging
import uuid

logging.basicConfig(
    level=logging.INFO,
    # filename="logs/log.log",
    # filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s)",
)

r_id = str(uuid.uuid4())

logging.debug(f"[request_id]: {r_id} - this is a debug message")
logging.info(f"[request_id]: {r_id} - this is an info message")
logging.warning(f"[request_id]: {r_id} - this is a warning message")
logging.error(f"[request_id]: {r_id} - this is an error message")
logging.critical(f"[request_id]: {r_id} - this is a critical message")


json_path_good_data = "data/sample_ok.json"
json_path_bad_data = "data/sample_bad.json"

result = read_json_file(json_path_good_data)

validated = validate_raw(result)

transformed_users = get_active_users(validated)
s_build = build_success(transformed_users)
print(s_build)
