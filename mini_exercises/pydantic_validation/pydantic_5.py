from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator,
    model_validator,
    ValidationError,
)


class Cart(BaseModel):
    model_config = ConfigDict(validate_assignment=True, extra="forbid")

    items: list[int] = Field(min_length=1)
    total: int = 0

    @field_validator("items")
    @classmethod
    def validate_items(cls, v):
        for i in v:
            if i < 0:
                raise ValueError("items can be only >= 0")
        return v

    @model_validator(mode="after")
    def compute_total(self):
        self.__dict__["total"] = sum(self.items)
        return self


try:
    c = Cart(items=[1, 2, 3])
    print(c)
except ValidationError as e:
    print("FAIL ", e.errors())
