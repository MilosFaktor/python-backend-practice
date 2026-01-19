import json


def extract_words(event):
    if "words" in event:
        words = event["words"]
        if isinstance(words, list):
            return words, ""
        return [], "'words' must be a list"

    if "body" in event:
        try:
            body = json.loads(event["body"])
        except json.JSONDecodeError:
            return [], "Invalid JSON in body"

        words = body.get("words")
        if isinstance(words, list):
            return words, ""
        return [], "'words' must be a list"

    return [], "'words' must be a list"


def clean_list_of_words(words):
    cleaned = []
    for i in words:
        i = i.strip()
        if i:
            cleaned.append(i)
    return cleaned


def count_words(cleaned_words):
    counts = {}
    for word in cleaned_words:
        counts[word] = counts.get(word, 0) + 1
    sorted_counts = dict(sorted(counts.items()))
    return sorted_counts


def output(raw, clean, counts, error):

    if error:
        return {
            "statusCode": 400,
            "body": json.dumps({"status": "error", "message": error}),
        }

    total_raw_count = len(raw)
    total_clean_count = len(clean)
    unique_clean_count = len(counts)

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "status": "success",
                "summary": {
                    "total_raw": total_raw_count,
                    "total_clean": total_clean_count,
                    "unique_clean": unique_clean_count,
                },
                "counts": counts,
            }
        ),
    }


def handler(event):
    words_list, error = extract_words(event)
    if error:
        return output([], [], {}, error)
    cleaned_words = clean_list_of_words(words_list)
    sorted_counts = count_words(cleaned_words)
    return output(words_list, cleaned_words, sorted_counts, error)


def main():
    event_A = {"words": [" apple ", "banana", "apple", "", "orange", "   "]}
    event_B = {"body": '{"words": [" apple ", "banana", "apple", "", "orange", "   "]}'}

    print(handler(event_A))
    print(handler(event_B))


if __name__ == "__main__":
    main()
