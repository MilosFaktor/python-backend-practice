# drill 1 basic schema
from pydantic import (
    BaseModel,
    ConfigDict,
)


class User(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
    )

    id: int
    name: str
    active: bool


data = {"id": "1", "name": "  John", "active": "true"}
user = User(**data)
print(user)
