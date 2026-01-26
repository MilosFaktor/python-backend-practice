# main.py

from xs14.ingest import read_json_file
from xs14.validate import validate_raw
from xs14.transform import get_active_users
from xs14.output import build_success, build_error
from xs14.logging_setup import setup_logging

import uuid


def main():
    r_id = str(uuid.uuid4())

    json_path_good_data = "data/sample_ok.json"
    json_path_bad_data = "data/sample_bad.json"

    result = read_json_file(json_path_good_data)

    validated = validate_raw(result)

    transformed_users = get_active_users(validated)
    s_build = build_success(transformed_users)
    print(s_build)
    logger = setup_logging("INFO")
    logger.info("hello")


if __name__ == "__main__":
    main()
