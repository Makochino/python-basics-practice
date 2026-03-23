from collections import deque

print("""Введите действие;\nНапишите "cancel" для отмены действия;\nВведите "exit" для завершения программы;""")
stack = deque()
running = True

while running:

    action = str(input("Введите ваш выбор из предложенных: "))

    if action == "exit":
        running = False
        print("Завершение работы ...")

    elif action == "cancel":
        if len(stack) > 0:
            removed = stack.pop()
            print("Порядок действий з изменениями:")
            for i, name in enumerate(stack, 1):
                print(f"{i}) {name}")
        else:
            print("Стек пустой действие не было отменено!!!")

    elif action.strip() == "":
        print("Действие не может быть пустой строкой!!!")

    else:
        stack.append(action)
        print("Порядок действий з изменениями:")
        for i, name in enumerate(stack, 1):
            print(f"{i}) {name}")


