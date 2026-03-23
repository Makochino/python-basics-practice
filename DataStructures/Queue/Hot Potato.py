from collections import deque

def hot_potato(players, passes):
    queue = deque(players)

    while len(queue) > 1:
        for _ in range(passes):
            queue.append(queue.popleft())  # передаем картошку дальше
        eliminated = queue.popleft()  # игрок выбывает
        print(f"{eliminated} выбыл(а) из игры.")

    print(f"\n🏆 Победитель: {queue[0]}")

players = deque(["Марк", "Илья", "Стас", "Григорий", "Василий", "Олег"])
passes = 5

hot_potato(players, passes)