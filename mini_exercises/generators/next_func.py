x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

y = map(lambda i: i**2, x)

print(next(y))
print(next(y))
print(next(y))
print(next(y))

print("For Loop Starts")

for i in y:  # continues loopint at 25 because of next() func
    print(i)
