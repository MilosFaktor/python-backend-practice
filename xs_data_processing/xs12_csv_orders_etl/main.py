import csv
from typing import Dict, List

CSV_INPUT = "orders.csv"
CSV_OUTPUT = "output_orders.csv"


def read_data_from_CSV() -> List[Dict]:
    orders = []
    with open(CSV_INPUT, newline="") as f:
        data = csv.DictReader(f)
        for row in data:
            orders.append(row)

    return orders


def validate_values(orders: List[Dict]) -> List[Dict]:
    if not isinstance(orders, list):
        raise TypeError("'orders' must be a list")
    if not orders:
        raise ValueError("'orders' must be populated")

    validated = []
    for order in orders:
        if not isinstance(order, dict):
            continue

        if not order:
            continue

        order_id = order.get("order_id")
        customer_id = order.get("customer_id")
        customer_name = order.get("customer_name")
        status = order.get("status")
        sku = order.get("sku")
        qty = order.get("qty")
        price = order.get("price")

        if not order_id or not order_id.strip():
            continue

        if not customer_id or not customer_id.isdigit():
            continue

        if not customer_name or not customer_name.strip():
            continue

        if not status or not status.strip():
            continue

        if not sku or not sku.strip():
            continue

        if not qty or not qty.strip():
            continue

        try:
            new_qty = int(qty)
            if not new_qty > 0:
                continue
        except ValueError:
            continue

        if not price or not price.strip():
            continue

        try:
            new_price = float(price)
            if not new_price >= 0:
                continue
        except ValueError:
            continue

        validated.append(order)

    return validated


def clean_values(validated_orders: List[Dict]) -> List[Dict]:
    if not validated_orders:
        raise ValueError("'orders' must be populated")
    if not isinstance(validated_orders, list):
        raise TypeError("'orders' must be a list")

    cleaned = []
    for order in validated_orders:
        new_order = dict(order)

        new_order["order_id"] = order.get("order_id").strip()
        new_order["customer_id"] = int(order.get("customer_id"))
        new_order["customer_name"] = order.get("customer_name").strip()
        new_order["status"] = order.get("status").strip()
        new_order["sku"] = order.get("sku").strip()
        new_order["qty"] = int(order.get("qty"))
        new_order["price"] = float(order.get("price"))

        cleaned.append(new_order)

    return cleaned


def build_structured_output(cleaned_orders: List[Dict]) -> List[Dict]:
    ordered_by_id = dict()

    for order in cleaned_orders:
        order_id = order.get("order_id")

        if order_id not in ordered_by_id:
            ordered_by_id[order_id] = {
                "order_id": order["order_id"],
                "customer": {
                    "id": order["customer_id"],
                    "name": order["customer_name"],
                },
                "items": [],
                "status": order["status"],
            }

        item = {"sku": order["sku"], "qty": order["qty"], "price": order["price"]}
        ordered_by_id[order_id]["items"].append(item)

    return list(ordered_by_id.values())

    """if not cleaned_orders:                                       # my solution
        raise ValueError("'orders' must be populated")
    if not isinstance(cleaned_orders, list):
        raise TypeError("'orders' must be a list")

    output = []
    ids = []
    for order in cleaned_orders:
        # print("INPUT:", order)
        new_order = dict()
        order_id = order.get("order_id")
        customer_id = order.get("customer_id")
        customer_name = order.get("customer_name")
        item_sku = order.get("sku")
        item_qty = order.get("qty")
        item_price = order.get("price")
        status = order.get("status")

        new_order["order_id"] = order_id
        if not order_id in ids:
            ids.append(order_id)

            customer = dict()
            customer["id"] = customer_id
            customer["name"] = customer_name
            new_order["customer"] = customer

            items = list()
            item = dict()
            item["sku"] = item_sku
            item["qty"] = item_qty
            item["price"] = item_price
            items.append(item)
            new_order["items"] = items

            new_order["status"] = status
            output.append(new_order)

        else:
            for o in output:  # order_id is in ids
                output_order_id = o.get("order_id")

                new_items = o.get("items")

                if not output_order_id == order_id:
                    # print("BLOCKED:", new_items)
                    continue

                item = dict()
                item["sku"] = item_sku
                item["qty"] = item_qty
                item["price"] = item_price
                new_items.append(item)
                break

                # print("PASSED:", new_items)

    return output"""


def main():
    raw_orders = read_data_from_CSV()
    validated_values = validate_values(raw_orders)
    cleaned_values = clean_values(validated_values)
    output = build_structured_output(cleaned_values)
    [print(o) for o in output]


if __name__ == "__main__":
    main()
