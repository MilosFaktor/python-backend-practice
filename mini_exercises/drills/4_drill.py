people = [
    ("Anna", "Berlin"),
    ("Peter", "London"),
    ("Eva", "Berlin"),
]
cities = {}

for name, city in people:
    if city not in cities:
        cities[city] = []
    cities[city].append(name)

print(cities)
