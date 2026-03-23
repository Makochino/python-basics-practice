def word_that_starts_with_a():
    words = ["Ant","babler","animal","ancient","DOg"]
    final = list(filter(lambda word: word.lower().startswith('a'), words))
    return final

def stealer(treasure):
    print(f"Отфильтрованный список: {treasure()}")

stealer(word_that_starts_with_a)
