def calc():
    while True:
        num1 = input("Введите первое число (или 'exit' для выхода): ")
        if num1.lower() == "exit":
          print("Программа завершена.")
          break
    
        num2 = input("Введите второе число: ")
        operation = input("Введите операцию (+, -, *, /): ")

        try:
            num1 = float(num1)
            num2 = float(num2)
    
        
            if operation == '+':
                print("Результат",num1 + num2)
            elif operation == '*':
                print("Результат",num1 * num2)
            elif operation == '-':
                print("Результат",num1 - num2)
            elif operation == '/':
                if num2 != 0:
                    print("Результат",num1 * num2)
                else:
                    print("Ошибка: Деление на ноль!")
            else:
                print("Ошибка неподдерижваемая операция!")

        except ValueError:
            print("Ошибка: Введите корректные числа!")
