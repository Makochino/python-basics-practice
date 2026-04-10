#filter usage
words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long_word(word):
    return len(word) > 4

long_words = list(filter(is_long_word, words))
print(long_words)

#map usage
numbers = [1,2,3,4,5,6,7]

def square(num):
    return num ** 2

square_numbers = list(map(square, numbers))
print(square_numbers)
