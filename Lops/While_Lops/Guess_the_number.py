import sys

low = 1
high = 100

while low <= high:
    mid = (low + high) // 2
    print(f"{mid}", flush=True)  # Відправляємо число інтерактору
    response = input().strip()  # Читаємо відповідь

    if response == "рівне":  # Число вгадане
        print(f"{mid}", flush=True)
        break
    elif response == "більше":  # Загадане число більше
        low = mid + 1
    elif response == "менше":  # Загадане число менше
        high = mid - 1