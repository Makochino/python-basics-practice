def fibonacci(n):
    if n <= 0:
        return "неверное ведь вы ввели 0"

    fib_1, fib_2 = 1, 1
    count = 2

    while count < n:
        fib_next = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = fib_next
        count += 1

    return fib_2

n = int(input("Введите число для ряда Фибоначчи ----> "))
print(f"Число по счету в ряду {n}: само число ряда {fibonacci(n)}")