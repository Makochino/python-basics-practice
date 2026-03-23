from collections import deque

def is_balanced(expression):
    stack = deque()
    brackets = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in brackets.values():
            stack.append(char)  # открывающая скобка
        elif char in brackets:
            if not stack or stack.pop() != brackets[char]:
                return False  # несоответствие или пустой стек

    return not stack  # если стек пуст — всё сбалансировано

# Примеры
expr1 = "(a + b) * [c - d]"
expr2 = "(a + b)) + ("

print(f"{expr1} ➤ {'✅' if is_balanced(expr1) else '❌'}")
print(f"{expr2} ➤ {'✅' if is_balanced(expr2) else '❌'}")
