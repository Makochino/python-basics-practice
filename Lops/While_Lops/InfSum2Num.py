end = ""

while end.lower() != "y":
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    print("Сумма числе:", num1 + num2)

    end = input("Нажмите Y или y для завершения программы: ")
    print("")
