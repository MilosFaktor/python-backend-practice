import json


def write_to_json_file(filename, content):
    with open(filename, "w") as f:
        json.dump(content, f, indent=2)


def read_and_clean_json_file(filename):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            total_words = data.get("words")
            if not isinstance(total_words, list):
                return [], [], "'words' must be a list"

            cleaned_words = []
            for word in total_words:
                word = word.strip()
                if word:
                    cleaned_words.append(word)
            return total_words, cleaned_words, ""

    except FileNotFoundError:
        return [], [], f"{filename} not found"

    except Exception:
        return [], [], "Something unexpected happened."


def count_words(words):
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    sorted_counts = dict(sorted(counts.items()))

    return sorted_counts


def build_output_dict(total_raw, total_clean, counts, e):
    raw = len(total_raw)
    clean = len(total_clean)
    unique = len(counts)

    if e:
        output = {
            "status": "error",
            "message": e,
        }
        return output

    output = {
        "status": "success",
        "summary": {"total_raw": raw, "total_clean": clean, "unique_clean": unique},
        "counts": counts,
    }
    return output


def write_output_to_json(filename, output):
    with open(filename, "w") as f:
        json.dump(output, f, indent=2)


def test_ipnut_file_doesnt_exist(input_file, output_file):
    total_raw, total_clean, e = read_and_clean_json_file(input_file)
    counts = count_words(total_clean)
    output = build_output_dict(total_raw, total_clean, counts, e)
    print(output)
    write_output_to_json(output_file, output)


def test_ipnut_file_exists(json_file, input_file, output_file):
    write_to_json_file(input_file, json_file)
    total_raw, total_clean, e = read_and_clean_json_file(input_file)
    counts = count_words(total_clean)
    output = build_output_dict(total_raw, total_clean, counts, e)
    print(output)
    write_output_to_json(output_file, output)


def main():
    json_file = {
        "words": [" apple ", "banana", "apple", "", "orange", "banana", "apple", "   "]
    }

    input_file = "input.json"
    output_file = "output.json"

    # test_ipnut_file_doesnt_exist(input_file, output_file)
    test_ipnut_file_exists(json_file, input_file, output_file)


if __name__ == "__main__":
    main()
