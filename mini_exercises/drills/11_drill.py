users = [
    {"name": "Anna", "age": 25, "score": 90},
    {"name": "Peter", "age": 31, "score": 90},
    {"name": "Eva", "age": 22, "score": 95},
    {"name": "Bob", "age": 20, "score": 90},
]

sorted_users = sorted(users, key=lambda u: (-u["score"], u["age"]))

for u in sorted_users:
    print(u)
