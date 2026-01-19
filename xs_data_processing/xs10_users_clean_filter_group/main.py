def clean_users(users: list[dict]) -> list[dict]:
    if not isinstance(users, list):
        raise TypeError("'users' must be a list")

    cleaned = []
    for line in users:
        if not isinstance(line, dict):
            raise TypeError("'line' in 'users' list must be a dict")

        if not "name" in line:
            raise ValueError("'name' value must be present")

        new_line = dict(line)
        new_line["name"] = new_line["name"].strip()
        if new_line["name"]:
            cleaned.append(new_line)

    return cleaned


def filter_active_users(users: list[dict]) -> list[dict]:
    filtered = []
    for user in users:
        if not "active" in user:
            raise ValueError("'active' must be specified")
        if not isinstance(user["active"], bool):
            raise TypeError("'active' must be a bool")

        if user["active"]:
            filtered.append(user)

    return filtered


def group_users_by_role(users: list[dict]) -> dict[str, list[dict]]:
    groups = {}
    for user in users:
        if "role" not in user:
            raise ValueError("'role' must be specified")
        role = user["role"]
        if role not in groups:
            groups[role] = []
        groups[role].append(user)

    return groups


def build_summary(groups: dict[str, list[dict]]) -> dict:

    summary = {"total_users": 0}
    for user_group, ls in groups.items():
        for user_dict in ls:
            summary["total_users"] += 1
            summary[user_group] = summary.get(user_group, 0) + 1

    return summary


def main():
    users = [
        {"id": 1, "name": " Alice ", "role": "admin", "active": True},
        {"id": 2, "name": "Bob", "role": "user", "active": False},
        {"id": 3, "name": "  Charlie", "role": "user", "active": True},
        {"id": 4, "name": "", "role": "admin", "active": True},
        {"id": 5, "name": "Eve", "role": "user", "active": True},
    ]

    cleaned_users = clean_users(users)
    print("Cleaned users:")
    for u in cleaned_users:
        print(u)
    print()

    active_users = filter_active_users(cleaned_users)
    print("Active users:")
    for u in active_users:
        print(u)
    print()

    grouped_users = group_users_by_role(active_users)
    print("Grouped_users:")
    print(grouped_users)
    print()

    summary = build_summary(grouped_users)
    print("Summary:")
    print(summary)
    print()


if __name__ == "__main__":
    main()
