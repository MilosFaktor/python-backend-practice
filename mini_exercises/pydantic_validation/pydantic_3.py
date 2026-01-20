# drill 3
from pydantic import (
    BaseModel,
    ConfigDict,
    field_validator,
    ValidationError,
    Field,
)


class Product(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        str_to_upper=True,
    )

    sku: str
    price: float = Field(gt=0)
    quantity: int = Field(ge=1)

    @field_validator("sku")
    @classmethod
    def validate_sku(cls, v):
        if len(v) != 6:
            raise ValueError("sku must be 6 chars like ABC123")
        if not v[:3].isalpha() or not v[3:].isdigit():
            raise ValueError("sku must be 3 letters + 3 digits (ABC123)")
        return v


tests = [
    {
        "sku": " abc123 ",
        "price": "10.5",
        "quantity": "2",
    },  # ✅ should pass (sku becomes ABC123)
    {"sku": "AB123", "price": 10, "quantity": 1},  # ❌ bad sku format
    {"sku": "ABC123", "price": 0, "quantity": 1},  # ❌ price must be > 0
    {"sku": "ABC123", "price": 5, "quantity": 0},  # ❌ quantity must be >= 1
    {"sku": "ABC123", "price": 5, "quantity": 1, "x": 1},  # ❌ extra field
]

for i, test in enumerate(tests, start=1):
    try:
        p = Product(**test)
        print(f"OK [{i}] {p}")
    except ValidationError as e:
        print(f"\nFAIL [{i}] {e.errors()}")
