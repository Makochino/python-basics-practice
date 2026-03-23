def reverse_string(s: str) -> str:
    reversed_str = []
    for char in s:
        reversed_str.insert(0, char)
    return "".join(reversed_str)

string = "hello"
reversed_string = reverse_string(string)
print("Reversed string --> ", reversed_string)
