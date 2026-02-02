nums_1 = [1, 2, 3, 4, 5, 6]
# → [4, 16, 36]
words_2 = ["a", "fast", "python", "is", "fun"]
# → [4, 6]
raw_3 = ["  A ", "", " B", "c  ", "   "]
# → ["a", "b", "c"]
nums_4 = [0, 1, 2, 3]
# → ["zero", "odd", "even", "odd"]
nums_5 = [3, -1, 5, -10, 2]
# → [3, 0, 5, 0, 2]

print(
    [n**2 for n in nums_1 if n % 2 == 0],
)
print(
    [len(w) for w in words_2 if len(w) > 3],
)
print(
    [w.strip().lower() for w in raw_3 if w.strip()],
)
print(
    ["zero" if n == 0 else "odd" if n % 2 == 1 else "even" for n in nums_4],
)
print(
    [n if n > 0 else 0 for n in nums_5],
)

nums_6 = [1, 2, 3, 4]
# → {1: 1, 2: 4, 3: 9, 4: 16}
words_7 = ["a", "fast", "python", "is"]
# → {"fast": 4, "python": 6}
nums_8 = [0, 1, 2, 3]
# → {0: "zero", 1: "odd", 2: "even", 3: "odd"}

print(
    {k: (k**2) for k in nums_6},
)
print(
    {w: (len(w)) for w in words_7 if len(w) > 3},
)
print(
    {n: "zero" if n == 0 else "odd" if n % 2 == 1 else "even" for n in nums_8},
)

matrix_9 = [[1, 2], [3, 4], [5]]
# → [1, 2, 3, 4, 5]
letters_10 = ["a", "b"]
nums_10 = [1, 2]
# → ["a1", "a2", "b1", "b2"]
matrix_11 = [[1, -2], [-3, 4], [5]]
# → [1, 4, 5]   # only positives

print(
    [i for ls in matrix_9 for i in ls],
)
print(
    [f"{le}{n}" for le in letters_10 for n in nums_10],
)
print(
    [i for ls in matrix_11 for i in ls if i > 0],
)
