from pydantic import BaseModel, ConfigDict, Field, field_validator


class UserRaw(BaseModel):
    model_config = ConfigDict(
        extra="forbid", validate_assignment=True, str_strip_whitespace=True
    )

    id: int = Field(ge=0)
    name: str = Field(min_length=1)
    active: bool

    @field_validator("id", mode="before")
    @classmethod
    def transform_id(cls, v):
        if isinstance(v, str):
            s = v.strip()
            if not s:
                raise ValueError("id str can not be empty")
            if s.isdigit():
                return int(s)
            else:
                raise ValueError("id str is not digit")
        elif isinstance(v, int):
            return v
        else:
            raise ValueError("Invalid id")

    @field_validator("active", mode="before")
    @classmethod
    def check_active(cls, v):
        if v is None:
            raise ValueError("active can not be None")
        if isinstance(v, str):
            if v.lower() == "true":
                return True
            elif v.lower() == "false":
                return False
            else:
                raise ValueError("active str can be only 'true'/'false'")
        elif isinstance(v, bool):
            return v
        else:
            raise ValueError("Invalid value in active")


class PayloadRaw(BaseModel):
    model_config = ConfigDict(extra="forbid", validate_assignment=True)

    message: list[UserRaw]


class UserOut(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True, validate_assignment=True)

    id: int
    name: str
