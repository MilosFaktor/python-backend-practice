from pydantic import BaseModel, Field, field_validator, ConfigDict, ValidationError
from typing import Literal
import json

raw_users = [
    {"id": "1", "name": " Alice ", "active": "true", "email": " alice@example.com "},
    {"id": 2, "name": "Bob", "active": False},
    {"id": "003", "name": "  Eva", "active": "FALSE", "email": ""},
    {"id": "x4", "name": "Chris", "active": "true"},  # bad id
    {"id": 5, "name": "   ", "active": True},  # bad name
    {"id": 6, "name": "Dana", "active": "yes"},  # bad active (must reject)
    {"id": -1, "name": "Frank", "active": True},  # bad id (negative)
    {"id": 7, "name": "Gina", "active": True, "hack": "x"},  # extra field (must reject)
]


class UserModel(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=False, validate_assignment=True)

    id: int = Field(ge=0)
    name: str
    email: str | None = None
    active: bool

    @field_validator("name")
    @classmethod
    def strip_name(cls, v: str) -> str:
        s = v.strip()
        if not s:
            raise ValueError("invalid 'name'")
        return s

    @field_validator("email", mode="before")
    @classmethod
    def strip_email(cls, v):
        if isinstance(v, str):
            s = v.strip()
            return s or None
        return v

    @field_validator("active", mode="before")
    @classmethod
    def active_accepts(cls, v):
        if isinstance(v, str):
            s = v.strip().lower()
            if s == "true":
                return True
            elif s == "false":
                return False
            else:
                raise ValueError("invalid 'active'")
        if isinstance(v, bool):
            return v
        else:
            raise ValueError("invalid 'active'")


def parse_users(
    raw_users: list[dict], policy: Literal["skip", "stop", "retry_once"] = "skip"
) -> tuple[list["UserModel"], list[dict]]:
    users: list[UserModel] = []
    errs: list[dict] = []

    for i, row in enumerate(raw_users):
        try:
            users.append(UserModel.model_validate(row))
        except ValidationError as e:
            if policy == "retry_once":
                try:
                    users.append(UserModel.model_validate(row))
                    continue
                except ValidationError as e2:
                    for err in e2.errors():
                        errs.append(
                            {
                                "index": i,
                                "field": err["loc"][0],
                                "message": err["msg"],
                            }
                        )
            else:
                for err in e.errors():
                    errs.append(
                        {
                            "index": i,
                            "field": err["loc"][0],
                            "message": err["msg"],
                        }
                    )

            if policy == "stop":
                break

    return (users, errs)


users, errs = parse_users(raw_users)
for u in users:
    print(u)

print()
for e in errs:
    print(e)
