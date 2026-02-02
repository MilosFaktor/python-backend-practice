def normalize_name(name):
    """
    "  Milos  " → "milos"
    ""         → None
    None       → None
    """
    if name is None:
        return None
    elif name.strip():
        return name.strip().lower()

    else:
        return None


def parse_int(value):
    """
    "10"  → 10
    10    → 10
    "x"   → None
    None  → None
    """
    if value is None:
        return None

    if isinstance(value, str) and value.isdigit():
        return int(value)

    if isinstance(value, int):
        return value

    return None
