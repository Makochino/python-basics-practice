sentence = "Hello my name is Maksim"

def count_words(s: str) -> int:
    string_list = s.split()
    return (len(string_list))



print(count_words(sentence))
