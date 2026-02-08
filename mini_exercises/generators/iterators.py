import sys

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


print(sys.getsizeof(x), "b")  # size 136

for element in x:
    print(element)

# iterator one
for i in range(1, 11):
    print(i)

print(sys.getsizeof(range(1, 11)))  # size 48

# iterator two
y = map(lambda i: i**2, x)  # map calls function on data structure returns an iterator

print(sys.getsizeof(y))  # size 48 doesnt need to store the sequence in memory
print(sys.getsizeof(list(y)))  # size 184 already generated whole list
