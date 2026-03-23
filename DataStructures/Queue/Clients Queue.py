from collections import deque

queue = deque(["МагнатВасилий", "Обеме228", "Калинатович"])
running = True
print("""Варианты выбора:
    1) Ввести имя клиента;
    2) Написать del — чтобы удалить последнего из очереди;
    3) Ввести exit — чтобы завершить работу;
""")

while running:

    choice = str(input("Ваш выбор: "))

    if choice == "exit":
        running = False
        print("Завершение работы ...")

    elif choice == "del" :
        if len(queue) > 0:
            removed = queue.popleft()
            print("Очередь з изменениями:")
            for i, name in enumerate(queue, 1):
                print(f"{i}) {name}")
        else:
            print("Очередь пуста никто не был удален.")

    elif choice.strip() == "":
        print("Имя клиента не может быть пустым.")

    else:
        queue.append(choice)
        print("Очередь з изменениями:")
        for i, name in enumerate(queue, 1):
            print(f"{i}) {name}")



