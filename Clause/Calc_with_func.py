import time

def get_values():   
    try:
        v1 = input("Enter first number (or 'q' to exit): ")
        if v1 == "q": return 'q', None, None
        num1 = float(v1)

        v2 = input("Enter second number (or 'q' to exit): ")
        if v2 == "q": return None, "q", None
        num2 = float(v2)

        op = input("Choice operation (+ - / // *) or q for exit: ")
        if op.lower() == 'q': return None, None, 'q'

        return num1, num2, op
                
    except ValueError:
            print("Ошибка: Вы ввели что-то нето )))) Попробуйте еще раз)")
            return None, None, "error"
            
def calculate(num1, num2, op):
    if op == "+": return("Result:", num1 + num2)
                
    elif op == "-": return("Result:", num1 - num2)
            
    elif op == "*": return("Result:", num1 * num2)
                 
    elif op == "/" or op == "//":
        if num2 == 0:
            return("Ошибка: деление на ноль невозможно!!!")
        else:
            result = num1 / num2 if op == "/" else num1//num2
            return("Result:", result)

    else: print(f"Ошибка: Оператион '{op}' не поддерживается пока что ;(\n\nUse from list: (+ - / // *)") 