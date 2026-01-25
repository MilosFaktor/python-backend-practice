# output.py

from xs14.models import UserOut
from xs14.errors import ErrorInfo


def build_success(users: list[UserOut]) -> dict:
    count = len(users)
    d_users = []
    for u in users:
        id = u.id
        name = u.name
        d_users.append({"id": id, "name": name})

    return {
        "statusCode": 200,
        "count": count,
        "users": d_users,
    }


def build_error(err: ErrorInfo) -> dict:
    status_code = err.status_code
    code = err.code
    message = err.message
    details = err.details

    return {
        "statusCode": status_code,
        "error": {
            "code": code,
            "message": message,
            "details": details,
        },
    }
