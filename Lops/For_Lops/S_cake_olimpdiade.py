a, b = map(int, input().split())  
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

found = False  # Флаг, найдено ли решение

for i in c:  
    for n in c:
        if a + b == i * n:
            print(i, n)
            found = True  # Запоминаем, что нашли пару

if not found:  # Если ни одна пара не нашлась, выводим -1 один раз
    print(-1)