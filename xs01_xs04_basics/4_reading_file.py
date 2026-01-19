with open("names.txt", "w") as f:
    f.write("Anna\nPeter\nMilos\nEva\nJohn\n")

with open("names.txt") as f:
    names = f.read().splitlines()
    l_names = len([n for n in names if len(n) > 4])
    print(f"{l_names} names are longer than 4 letters")
