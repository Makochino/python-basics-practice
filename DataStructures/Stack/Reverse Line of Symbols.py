from collections import deque

text = input("введите текст: ")
stack = deque()

for char in text:
    stack.append(char)

reversed_text = ""

while stack:
    reversed_text += stack.pop()

print(reversed_text)