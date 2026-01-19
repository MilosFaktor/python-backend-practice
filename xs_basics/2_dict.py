people = {"Anna": "London", "Peter": "Berlin", "Eva": "Paris", "Milos": "Berlin"}

in_Berlin = 0
for name, city in people.items():
    if city == "Berlin":
        print(f"{name} lives in {city}.")
        in_Berlin += 1
    else:
        print(f"{name} lives in {city}.")

print(f"{in_Berlin} people live in Berlin.")
