text = input("Введите строку: ").split()
words_count = {}

for word in text:
    if word in words_count:
        words_count[word] += 1
    else:
        words_count[word] = 1

print(words_count)
