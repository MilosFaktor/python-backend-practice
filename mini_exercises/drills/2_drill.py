text = "apple,banana,,orange"
words = []
word = ""
for ch in text:
    if ch == ",":
        words.append(word)
        word = ""
    else:
        word += ch
if word:
    words.append(word)


clean = [w for w in words if w]
print(clean)
