# test_transform.py

from xs14.transform import get_active_users
from xs14.models import UserOut
from xs14.validate import validate_raw


def test_filter_active_users():
    """Filters only active users"""
    payload_raw = {
        "message": [
            {"id": "1", "name": "Alice", "active": "true"},
            {"id": "2", "name": "Alice", "active": "false"},
            {"id": "3", "name": "Alice", "active": "false"},
            {"id": "4", "name": "Alice", "active": "true"},
            {"id": "5", "name": "Alice", "active": "false"},
            {"id": "6", "name": "Alice", "active": "true"},
        ]
    }
    validated = validate_raw(payload_raw)
    result = get_active_users(validated)

    assert [u.id for u in result] == [1, 4, 6]
    assert len(result) == 3


def test_output_model_mapping():

    payload_raw = {"message": [{"id": "1", "name": "Alice", "active": "true"}]}
    validated = validate_raw(payload_raw)
    result = get_active_users(validated)

    assert isinstance(result, list)
    assert len(result) == 1

    u = result[0]
    assert isinstance(u, UserOut)
    assert hasattr(u, "id")
    assert hasattr(u, "name")
    assert not hasattr(u, "active")
