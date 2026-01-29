# validate.py

from pydantic import ValidationError
from xs14.models import PayloadRaw
from xs14.errors import ErrorInfo


def validate_raw(raw_data: dict) -> PayloadRaw | ErrorInfo:
    try:
        validated = PayloadRaw.model_validate(raw_data)
        return validated

    except ValidationError as e:
        errors_l = []
        for errs in e.errors():
            type_ = errs.get("type")
            loc_ = errs.get("loc")
            msg_ = errs.get("msg")
            errors_l.append({"type": type_, "loc": loc_, "msg": msg_})

        return ErrorInfo(
            status_code=400,
            code="VALIDATION_ERROR",
            message="Invalid input payload",
            details=errors_l,
        )
