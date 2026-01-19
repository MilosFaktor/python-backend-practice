def write_words_to_file(filename, words):
    with open(filename, "w") as f:
        for w in words:
            f.write(w + "\n")


def read_words_from_file(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


def count_words(words):
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return counts


def write_counts_to_file(filename, counts):
    with open(filename, "w") as f:
        for name, count in counts.items():
            suffix = "time" if count == 1 else "times"
            f.write(f"{name} appears {count} {suffix}\n")


def main():
    items = [
        "apple",
        "banana",
        "apple",
        "orange",
        "banana",
        "apple",
        "strawberry",
        "peach",
        "peach",
    ]

    input_file = "words.txt"
    output_file = "results.txt"

    write_words_to_file(input_file, items)
    words = read_words_from_file(input_file)
    counts = count_words(words)
    write_counts_to_file(output_file, counts)
    with open(output_file, "r") as f:
        print(f.read())


if __name__ == "__main__":
    main()
