# drill 4 nested model + derived field
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    ValidationError,
    computed_field,
)


class Customer(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True, extra="forbid", str_strip_whitespace=True
    )
    id: int
    name: str = Field(min_length=1)


class OrderItem(BaseModel):
    model_config = ConfigDict(validate_assignment=True, extra="forbid")

    product_id: str
    price: float = Field(gt=0)
    quantity: int = Field(ge=1)


class Order(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True, extra="forbid", str_strip_whitespace=True
    )
    order_id: str
    customer: Customer
    items: list[OrderItem] = Field(min_length=1)

    # NOTE: total is NOT a field, so input "total" will fail due to extra="forbid"
    @computed_field
    @property
    def total(self) -> float:
        return sum(item.price * item.quantity for item in self.items)


data_2 = [
    # 1) ✅ valid (your baseline)
    {
        "order_id": "ORD-1",
        "customer": {"id": "10", "name": "  milos  "},
        "items": [
            {"product_id": "A", "price": "10", "quantity": 2},
            {"product_id": "B", "price": 5, "quantity": 1},
        ],
    },
    # 2) ❌ items empty (min_length=1 should fail)
    {
        "order_id": "ORD-EMPTY",
        "customer": {"id": 1, "name": "John"},
        "items": [],
    },
    # 3) ❌ customer name empty after strip (min_length=1 should fail)
    {
        "order_id": "ORD-NAME",
        "customer": {"id": 1, "name": "   "},
        "items": [{"product_id": "A", "price": 1, "quantity": 1}],
    },
    # 4) ❌ negative price (gt=0 should fail)
    {
        "order_id": "ORD-NEGPRICE",
        "customer": {"id": 1, "name": "John"},
        "items": [{"product_id": "A", "price": -1, "quantity": 1}],
    },
    # 5) ❌ quantity zero (ge=1 should fail)
    {
        "order_id": "ORD-ZEROQ",
        "customer": {"id": 1, "name": "John"},
        "items": [{"product_id": "A", "price": 1, "quantity": 0}],
    },
    # 6) ❌ extra field at top level (extra="forbid")
    {
        "order_id": "ORD-EXTRA-TOP",
        "customer": {"id": 1, "name": "John"},
        "items": [{"product_id": "A", "price": 1, "quantity": 1}],
        "status": "paid",
    },
    # 7) ❌ extra field inside customer (extra="forbid" applies in nested too)
    {
        "order_id": "ORD-EXTRA-CUST",
        "customer": {"id": 1, "name": "John", "vip": True},
        "items": [{"product_id": "A", "price": 1, "quantity": 1}],
    },
    # 8) ❌ extra field inside item
    {
        "order_id": "ORD-EXTRA-ITEM",
        "customer": {"id": 1, "name": "John"},
        "items": [{"product_id": "A", "price": 1, "quantity": 1, "x": 123}],
    },
    # 9) ❌ total passed in input (should be rejected because total is computed, not a field)
    {
        "order_id": "ORD-TOTAL-IN",
        "customer": {"id": 1, "name": "John"},
        "items": [{"product_id": "A", "price": 1, "quantity": 1}],
        "total": 999,
    },
    # 10) ✅ valid: numeric strings everywhere (casting test)
    {
        "order_id": "ORD-CAST",
        "customer": {"id": "99", "name": "  Eva "},
        "items": [{"product_id": "X", "price": "2.5", "quantity": "4"}],
    },
]

for i, d in enumerate(data_2, start=1):
    try:
        o = Order(**d)
        print(f"OK [{i}] {o}")
    except ValidationError as e:
        print(f"\nFAIL [{i}] {e.errors()}")
