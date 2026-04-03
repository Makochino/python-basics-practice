from array import *

numbers = array('i', [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

while True:
    try:
        chosen_number = int(input("Введите число которое нужно будет найти до 400 путем умножения: "))

        if chosen_number == 0:
            print("Выход из программы")
            break

        found = False
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                num1 = numbers[i]
                num2 = numbers[j]
                if num1 * num2 == chosen_number:
                    print(f"Пара найдена: {num1} * {num2} = {chosen_number}")
                    found = True

        if not found:
            print(print("❌ Невозможно найти пару чисел с таким умножением."))

    except ValueError:
        print("Введи сучка целое число!!!!!")
