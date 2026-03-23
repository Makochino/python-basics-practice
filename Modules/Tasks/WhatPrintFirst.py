x = 10

def outer():
    x = 20  # Переменная уровня enclosing
    def inner():
        x = 30  # Локальная переменная
        print(x)  

    inner()

outer()
print(x)  