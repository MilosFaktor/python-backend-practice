# test_integration_flow.py

from xs14.ingest import read_json_file
from xs14.validate import validate_raw
from xs14.transform import get_active_users
from xs14.output import build_success, build_error
from xs14.errors import ErrorInfo


def test_happy_path():
    json_path_good_data = "data/sample_ok.json"
    raw = read_json_file(json_path_good_data)
    validated = validate_raw(raw)
    active_users = get_active_users(validated)
    result = build_success(active_users)

    assert result == {
        "statusCode": 200,
        "count": 5,
        "users": [
            {"id": 1, "name": "Alice"},
            {"id": 3, "name": "Charlie"},
            {"id": 4, "name": "Diana"},
            {"id": 6, "name": "Frank"},
            {"id": 8, "name": "Heidi"},
        ],
    }


def test_bad_input():
    json_path_bad_data = "data/sample_bad.json"
    raw = read_json_file(json_path_bad_data)
    error = validate_raw(raw)

    assert isinstance(error, ErrorInfo)

    result = build_error(error)

    assert result == {
        "statusCode": 400,
        "error": {
            "code": "VALIDATION_ERROR",
            "message": "Invalid input payload",
            "details": [
                {
                    "type": "missing",
                    "loc": ("message", 7, "active"),
                    "msg": "Field required",
                },
                {
                    "type": "extra_forbidden",
                    "loc": ("message", 7, "actve"),
                    "msg": "Extra inputs are not permitted",
                },
            ],
        },
    }
