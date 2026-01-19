words = ["apple", "banana", "apple", "orange", "banana", "apple"]

counts = {}

for w in words:
    counts[w] = counts.get(w, 0) + 1

print(counts)

for key, value in counts.items():
    if value == 1:
        print(f"{key} appears {value} time")
    else:
        print(f"{key} appears {value} times")

items = ["apple", "banana", "apple", "orange", "banana", "apple", "strawberry"]
f_name = "words.txt"

with open(f_name, "w") as f:
    for i in items:
        f.write(i + "\n")

counts = {}
with open(f_name, "r") as f:
    words = f.read().splitlines()

    for w in words:
        counts[w] = counts.get(w, 0) + 1

with open("results.txt", "w") as f:
    for name, count in counts.items():
        suffix = "time" if count == 1 else "times"
        f.write(f"{name} appears {count} {suffix}\n")

with open("results.txt", "r") as f:
    content = f.read()
    print(content)
