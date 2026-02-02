nums = [0, 1, 2, 3, 4, 5, -2, -3]

for n in nums:
    labels = []

    if n == 0:
        labels.append("zero")
    else:
        if n % 2 == 0:
            labels.append("even")
        else:
            labels.append("odd")

    if n < 0:
        labels.append("negative")

    print(f"{n} -> {', '.join(labels)}")
