from array import *

try:
    selected_number = int(input("Введите целое число от 1 до 10: "))
except ValueError:
    print("Ошибка: тип данных не соответствует — нужно ввести ЦЕЛОЕ ЧИСЛО.")
    exit()

numbers = array('i', [2,3,4,5,6,7,1,9,8])

found = False

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        num1 = numbers[i]
        num2 = numbers[j]
        if num1 + num2 == selected_number:
            print(f"✅ Пара найдена: {num1} + {num2} = {selected_number}")
            found = True

if not found:
    print("❌ Число введенное вами не может быть получено как сумма двух чисел из массива.")
