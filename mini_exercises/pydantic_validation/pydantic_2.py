# drill 2
from pydantic import (
    BaseModel,
    ConfigDict,
    field_validator,
    ValidationError,
)


class User_1(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
    )

    id: int
    name: str
    active: bool
    email: str | None = None
    age: int | None = None

    @field_validator("email")
    @classmethod
    def validate_email(cls, v):
        if v is None:
            return None
        if not "@" in v:
            raise ValueError("email must contain @")
        return v

    @field_validator("age")
    @classmethod
    def validate_age(cls, v):
        if v is None:
            return None
        if not v >= 18:
            raise ValueError("age must be >= 18")
        return v


data_1 = [
    {
        "id": "1",
        "name": "  John  ",
        "active": "true",
        "email": " john@x.com ",
        "age": "18",
    },
    {"id": 2, "name": "Eva", "active": False},
    {"id": 3, "name": "A", "active": True, "email": "not-an-email"},
    {"id": 4, "name": "B", "active": True, "age": 17},
    {"id": 5, "name": "C", "active": True, "role": "admin"},
]

for i, user in enumerate(data_1, start=1):
    try:
        u = User_1(**user)
        print(f"{i}, {u}")
    except ValidationError as e:
        print(f"{i}, {e}")
