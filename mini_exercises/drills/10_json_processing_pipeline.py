import json
from json import JSONDecodeError

input_file = "input_users.json"
outpput_file = "output.json"


def read_json(input: str) -> dict | None:
    try:
        with open(input, "r") as f:
            payload = json.load(f)
            return payload
    except JSONDecodeError:
        print("ERROR: Invalid JSON")
    except FileNotFoundError:
        print("ERROR: File not found")


def process_users(data: dict) -> dict:
    if not isinstance(data, dict):
        raise TypeError("Raw must be dict")
    if not data:
        raise ValueError("Raw must not be empty")

    if "users" not in data:
        raise ValueError("Raw must have 'users'")
    if not isinstance(data["users"], list):
        raise TypeError("'users' must be a list")
    if not data["users"]:
        raise ValueError("users can not be empty")

    total_in = 0
    total_out = 0

    users = []
    for u in data["users"]:
        total_in += 1
        valid_user = transform_user(u)
        if not valid_user:
            continue

        total_out += 1
        users.append(valid_user)

    skipped = total_in - total_out

    return {
        "total_in": total_in,
        "total_out": total_out,
        "skipped": skipped,
        "users": users,
    }


def transform_user(raw: dict) -> dict | None:
    if not isinstance(raw, dict):
        return None
    if not raw:
        return None

    must_have = ["id", "name", "age", "active"]
    for condition in must_have:
        if condition not in raw:
            return None

    user = dict()

    if not raw["id"]:
        return None
    if isinstance(raw["id"], str):
        if not raw["id"].isdigit():
            return None
        i = int(raw["id"])
        user["id"] = i
    elif isinstance(raw["id"], int):
        if raw["id"] >= 0:
            i = int(raw["id"])
            user["id"] = i
    else:
        return None

    if isinstance(raw["name"], str):
        if not raw["name"].strip():
            return None
        name = str(raw["name"].strip().title())
        user["name"] = name
    else:
        return None

    if not raw["age"]:
        return None
    if isinstance(raw["age"], str):
        if not raw["age"].isdigit():
            return None
        i = int(raw["age"])
        user["age"] = i
    elif isinstance(raw["age"], int):
        if raw["age"] >= 0:
            i = int(raw["age"])
            user["age"] = i
    else:
        return None

    if raw["active"].lower() == "true":
        user["active"] = True
    elif raw["active"].lower() == "false":
        user["active"] = False
    else:
        user["active"] = False

    return user


def write_json(path, data) -> None:
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


def main():
    raw = read_json(input_file)
    if not raw:
        print("can't procceed further. ERROR in read_json()")
    else:
        print("read_json() success: procceeding further")
        data = process_users(raw)
        if not data:
            print("can't procceed further. ERROR in process_users()")
        else:
            print("process_users() success: procceeding further")
            write_json(outpput_file, data)


if __name__ == "__main__":
    main()
