from typing import TypedDict, NotRequired, Literal
from dataclasses import dataclass

raw_users = [
    {"id": "1", "name": " Alice ", "active": "true", "email": " alice@example.com "},
    {"id": 2, "name": "Bob", "active": False},
    {"id": "003", "name": "  Eva", "active": "FALSE", "email": ""},
    {"id": "x4", "name": "Chris", "active": "true"},  # bad id
    {"id": 5, "name": "   ", "active": True},  # bad name
    {"id": 6, "name": "Dana", "active": "yes"},  # bad active
    {"id": None, "name": "Frank", "active": True},  # bad id type
]


class RawUser(TypedDict):
    id: str | int
    name: str
    active: str | bool
    email: NotRequired[str]


@dataclass(frozen=True, slots=True)
class User:
    id: int
    name: str
    active: bool
    email: str | None = None


raw: RawUser = {
    "id": "1",
    "name": " Alice ",
    "active": "true",
    "email": " alice@example.com ",
}


def normalize_user(raw: RawUser) -> User:
    raw_id = raw["id"]
    raw_name = raw["name"]
    raw_active = raw["active"]
    raw_email = raw.get("email")

    if isinstance(raw_id, str):
        new_id = raw_id.strip()
        if not new_id.isdigit():
            raise ValueError("invalid id")
        id_ = int(new_id)
    elif isinstance(raw_id, int):
        if raw_id >= 0:
            id_ = raw_id
        else:
            raise ValueError("invalid id")
    else:
        raise ValueError("invalid id")

    name_ = raw_name.strip()
    if not name_:
        raise ValueError("invalid name")

    if isinstance(raw_active, str):
        new_active = raw_active.strip().lower()
        if not new_active:
            raise ValueError("invalid active")
        if new_active == "true":
            active_ = True
        elif new_active == "false":
            active_ = False
        else:
            raise ValueError("invalid active")
    elif isinstance(raw_active, bool):
        active_ = raw_active
    else:
        raise ValueError("invalid active")

    if raw_email is None:
        email_ = None
    else:
        new_email = raw_email.strip()
        email_ = new_email if new_email else None

    return User(id=id_, name=name_, active=active_, email=email_)


def normalize_users(
    raw_users: list[RawUser], policy: Literal["skip", "stop", "retry_once"] = "skip"
) -> tuple[list[User], list[str]]:
    valid_users = []
    errors = []
    for i, u in enumerate(raw_users):
        try:
            user = normalize_user(u)
            valid_users.append(user)
        except ValueError as e:
            if policy == "retry_once":
                try:
                    user = normalize_user(u)
                    valid_users.append(user)
                    continue
                except ValueError as e2:
                    errors.append(f"index: {i}, Value error: {str(e2)}")
            else:
                errors.append(f"index: {i}, Value error: {str(e)}")

            if policy == "stop":
                break

    return (valid_users, errors)


usrs, errs = normalize_users(raw_users, "stop")
print(usrs, "\n\n", errs)
