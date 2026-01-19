from typing import Dict, List, Tuple


def clean_orders(orders) -> List[Dict]:
    if not isinstance(orders, list):
        raise TypeError("'orders' must be a list")
    if not orders:
        raise ValueError("'orders' list can not be empty")
    cleaned_orders = []

    for order in orders:  # order is a Dict
        if not isinstance(order, dict):
            continue

        customer = order.get("customer")
        items = order.get("items")

        if not isinstance(customer, dict):
            continue

        if not isinstance(items, list):
            continue

        if not items:
            continue

        name = customer.get("name")
        if not isinstance(name, str):
            continue

        name = name.strip()
        if not name:
            continue

        new_order = dict(order)
        new_order["customer"] = dict(customer)
        new_order["customer"]["name"] = name

        cleaned_orders.append(new_order)

    return cleaned_orders


def calculate_order_total(order: Dict) -> float:
    if not isinstance(order, dict):
        raise TypeError("'order' must be a dict")
    if not order:
        raise ValueError("'order' must be populated")

    items = order.get("items")
    if not isinstance(items, list):
        raise TypeError("'items' must be a list")

    order_total = 0.0
    for item in items:

        qty = item.get("qty")
        price = item.get("price")

        if not isinstance(qty, (int, float)):
            continue
        if qty < 0:
            continue

        if not isinstance(price, (int, float)):
            continue
        if price < 0:
            continue

        order_total += float(qty * price)

    return order_total


def build_customer_spend_report(orders) -> Dict:
    if not isinstance(orders, list):
        raise TypeError("'orders' must be a list")
    if not orders:
        raise ValueError("'orders' must be populated")

    report = {}
    for order in orders:
        if not isinstance(order, dict):
            continue

        if not order:
            continue

        status = order.get("status")
        customer = order.get("customer")  # already checked in cleaning funtion
        customer_id = customer.get("id")

        if not isinstance(customer_id, int):
            continue

        if customer_id < 0:
            continue

        if not isinstance(status, str) or not status:
            continue

        if not status == "paid":
            continue

        order_total = calculate_order_total(order)
        report[customer_id] = report.get(customer_id, 0.0) + order_total

    return report


def top_customer(report) -> Tuple[int | None, float]:
    best_customer = tuple()
    if not isinstance(report, dict):
        raise TypeError("'report' must be a dictionary")
    if not report:
        return (None, 0.0)

    for id, amount in report.items():
        if not best_customer:
            best_customer = int(id), float(amount)

        if best_customer[1] < amount:
            best_customer = int(id), float(amount)

    return best_customer


def main():
    orders_1 = [
        {
            "order_id": "A100",
            "customer": {"id": 1, "name": " Alice "},
            "items": [
                {"sku": "X", "qty": 2, "price": 10.0},
                {"sku": "Y", "qty": 1, "price": 5.0},
            ],
            "status": "paid",
        },
        {
            "order_id": "A101",
            "customer": {"id": 2, "name": "Bob"},
            "items": [{"sku": "X", "qty": 1, "price": 10.0}],
            "status": "pending",
        },
        {
            "order_id": "A102",
            "customer": {"id": 3, "name": "  Charlie"},
            "items": [],
            "status": "paid",
        },
        {
            "order_id": "A103",
            "customer": {"id": 4, "name": ""},
            "items": [{"sku": "Z", "qty": 3, "price": 7.0}],
            "status": "paid",
        },
        {
            "order_id": "A104",
            # customer missing on purpose
            "items": [{"sku": "X", "qty": 2, "price": 10.0}],
            "status": "paid",
        },
    ]

    orders_2 = [
        {
            "order_id": "A200",
            "customer": {"id": 1, "name": " Alice "},
            "items": [
                {"sku": "X", "qty": 2, "price": 10.0},
                {"sku": "Y", "qty": 1, "price": 5.0},
            ],
            "status": "paid",
        },
        {
            "order_id": "A201",
            "customer": {"id": 1, "name": "Alice"},
            "items": [
                {"sku": "Z", "qty": 3, "price": 7.0},
            ],
            "status": "paid",
        },
        {
            "order_id": "A202",
            "customer": {"id": 2, "name": " Bob "},
            "items": [
                {"sku": "X", "qty": 1, "price": 10.0},
            ],
            "status": "pending",
        },
        {
            "order_id": "A203",
            "customer": {"id": 2, "name": "Bob"},
            "items": [
                {"sku": "Y", "qty": 2, "price": 5.0},
            ],
            "status": "paid",
        },
        {
            "order_id": "A204",
            "customer": {"id": 3, "name": "  Charlie"},
            "items": [
                {"sku": "X", "qty": 1, "price": 10.0},
                {"sku": "Y", "qty": 1, "price": 5.0},
            ],
            "status": "paid",
        },
        {
            "order_id": "A205",
            "customer": {"id": 3, "name": "Charlie"},
            "items": [],
            "status": "paid",
        },
        {
            "order_id": "A206",
            "customer": {"id": 4, "name": ""},
            "items": [
                {"sku": "Z", "qty": 2, "price": 7.0},
            ],
            "status": "paid",
        },
        {
            "order_id": "A207",
            "customer": {"id": 5, "name": " Eve "},
            "items": [
                {"sku": "X", "qty": 2, "price": 10.0},
                {"sku": "Y", "qty": -1, "price": 5.0},  # invalid qty
            ],
            "status": "paid",
        },
        {
            "order_id": "A208",
            "customer": {"id": 5, "name": "Eve"},
            "items": [
                {"sku": "Z", "qty": 1, "price": 7.0},
            ],
            "status": "paid",
        },
        {
            "order_id": "A209",
            # customer missing on purpose
            "items": [
                {"sku": "X", "qty": 2, "price": 10.0},
            ],
            "status": "paid",
        },
    ]

    clean = clean_orders(orders_2)
    print("Cleaned:")
    for c in clean:
        print(c)
    print()

    report = build_customer_spend_report(clean)
    print("Customer report:")
    print(report)
    print()

    best_customer = top_customer(report)
    print("Top customer:")
    print(best_customer)
    print()

    return best_customer


if __name__ == "__main__":
    main()
