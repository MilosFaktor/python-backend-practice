data = {"a": 1, "b": 2, "c": 1}

goal = {}

for ch, n in data.items():
    if n not in goal:
        goal[n] = []
    goal[n].append(ch)

print(goal)
