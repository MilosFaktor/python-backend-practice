# test_output.py

from xs14.output import build_success, build_error
from xs14.transform import get_active_users
from xs14.validate import validate_raw
from xs14.errors import ErrorInfo


def test_build_success_shape():
    payload_raw = {"message": [{"id": "1", "name": "Alice", "active": "true"}]}
    validated = validate_raw(payload_raw)
    filtered = get_active_users(validated)
    result = build_success(filtered)

    assert result == {
        "statusCode": 200,
        "count": 1,
        "users": [{"id": 1, "name": "Alice"}],
    }


def test_build_success_count():
    payload_raw = {
        "message": [
            {"id": "1", "name": "Alice", "active": "true"},
            {"id": "2", "name": "Alice", "active": "false"},
            {"id": "3", "name": "Alice", "active": "true"},
            {"id": "4", "name": "Alice", "active": "false"},
        ]
    }
    validated = validate_raw(payload_raw)
    filtered = get_active_users(validated)
    result = build_success(filtered)

    assert result["statusCode"] == 200
    assert result["count"] == 2
    assert result == {
        "statusCode": 200,
        "count": 2,
        "users": [{"id": 1, "name": "Alice"}, {"id": 3, "name": "Alice"}],
    }


def test_build_error_shape():
    payload_raw = {"message": [{"id": -1, "name": "Alice", "active": "true"}]}
    error = validate_raw(payload_raw)

    assert isinstance(error, ErrorInfo)

    result = build_error(error)

    assert result["statusCode"] == 400
    assert isinstance(result["error"], dict)
    assert "code" in result["error"]
    assert "message" in result["error"]
    assert "details" in result["error"]
