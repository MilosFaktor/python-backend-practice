# test_validate.py

from xs14.validate import validate_raw
from xs14.models import PayloadRaw
from xs14.errors import ErrorInfo


def test_validate_id_parsing():
    """Testing id parsing"""
    result_1 = validate_raw(
        {"message": [{"id": "1", "name": "Alice", "active": "true"}]}
    )
    result_2 = validate_raw(
        {"message": [{"id": -1, "name": "Alice", "active": "true"}]}
    )
    result_3 = validate_raw(
        {"message": [{"id": "", "name": "Alice", "active": "true"}]}
    )
    result_4 = validate_raw(
        {"message": [{"id": "true", "name": "Alice", "active": "true"}]}
    )
    result_5 = validate_raw(
        {"message": [{"id": True, "name": "Alice", "active": "true"}]}
    )

    assert isinstance(result_1, PayloadRaw)
    assert isinstance(result_2, ErrorInfo)
    assert isinstance(result_3, ErrorInfo)
    assert isinstance(result_4, ErrorInfo)
    assert isinstance(result_5, ErrorInfo)

    assert result_1.message[0].id == 1
    assert result_2.code == "VALIDATION_ERROR"
    assert result_3.details[0]["msg"] == "Value error, id str can not be empty"
    assert result_4.details[0]["msg"] == "Value error, id str is not digit"
    assert result_5.details[0]["msg"] == "Value error, id can not be bool"


def test_validate_active_parsing():
    """Testing active parsing"""
    result_6 = validate_raw({"message": [{"id": 1, "name": "Alice", "active": "true"}]})
    result_7 = validate_raw(
        {"message": [{"id": 1, "name": "Alice", "active": "false"}]}
    )
    result_8 = validate_raw({"message": [{"id": 1, "name": "Alice", "active": "x"}]})

    assert isinstance(result_6, PayloadRaw)
    assert isinstance(result_7, PayloadRaw)
    assert isinstance(result_8, ErrorInfo)

    assert result_6.message[0].active is True
    assert result_7.message[0].active is False
    assert (
        result_8.details[0]["msg"]
        == "Value error, active str can be only 'true'/'false'"
    )


def test_validate_name_rules():
    """Testing name striping + empty check"""
    result_9 = validate_raw(
        {"message": [{"id": 1, "name": " Alice ", "active": "true"}]}
    )
    result_10 = validate_raw({"message": [{"id": 1, "name": "  ", "active": "true"}]})
    result_11 = validate_raw({"message": [{"id": 1, "name": 1, "active": "true"}]})

    assert isinstance(result_9, PayloadRaw)
    assert isinstance(result_10, ErrorInfo)
    assert isinstance(result_11, ErrorInfo)

    assert result_9.message[0].name == "Alice"
    assert result_10.details[0]["msg"] == "String should have at least 1 character"
    assert result_11.details[0]["msg"] == "Input should be a valid string"


def test_validate_message_field():
    """Testing top level message"""
    result_12 = validate_raw({"": []})
    result_13 = validate_raw({"message": []})

    assert isinstance(result_12, ErrorInfo)
    assert isinstance(result_13, PayloadRaw)

    assert result_12.details[0]["msg"] == "Field required"
    assert result_13.message == []
