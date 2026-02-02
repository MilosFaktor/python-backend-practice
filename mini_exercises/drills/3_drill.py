sentence = "python is fast"

words = []
word = ""
for ch in sentence:
    if ch == " ":
        words.append(word)
        word = ""
    else:
        word += ch
if word:
    words.append(word)


reordered = []
for _ in words:
    reordered.append("")

start = -1
for i, w in enumerate(words):
    reordered[start] = w
    start -= 1

print(" ".join(reordered))
