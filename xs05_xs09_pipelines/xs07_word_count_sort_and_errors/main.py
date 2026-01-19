def write_words_to_file(filename, words):
    with open(filename, "w") as f:
        for w in words:
            f.write(w + "\n")


def read_words_from_file(filename):
    try:
        with open(filename, "r") as f:
            words = f.read().splitlines()
    except FileNotFoundError:
        print(f"Error: '{filename}' not found")
        return []

    cleaned = []
    for w in words:
        w = w.strip()
        if w:
            cleaned.append(w)
    return cleaned


def count_words(words):
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return counts


def write_counts_to_file_sorted_alphabetically(filename, operator, counts):
    with open(filename, operator) as f:
        for word in sorted(counts):
            count = counts[word]
            suffix = "time" if count == 1 else "times"
            f.write(f"{word} appears {count} {suffix}\n")


def write_counts_to_file_sorted_numerically_reversed(filename, operator, counts):
    with open(filename, operator) as f:
        sorted_items = sorted(
            counts.items(),
            key=lambda item: item[1],
            reverse=True,
        )

        for word, count in sorted_items:
            suffix = "time" if count == 1 else "times"
            f.write(f"{word} appears {count} {suffix}\n")


def append_empty_line(filename):
    with open(filename, "a") as f:
        f.write("\n")


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
    if not words:
        print("No words to process.")
        return
    counts = count_words(words)

    write_counts_to_file_sorted_alphabetically(output_file, "w", counts)
    append_empty_line(output_file)

    write_counts_to_file_sorted_numerically_reversed(output_file, "a", counts)
    with open(output_file, "r") as f:
        print(f.read())


if __name__ == "__main__":
    main()
