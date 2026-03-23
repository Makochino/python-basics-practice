string = "Game is really intersting"

def swap_first_last(s: str) -> str:
    list_words = s.split()
    empty_list = []
    for word in list_words:
        empty_list.append(word[-1])

    return empty_list

print(swap_first_last(string))