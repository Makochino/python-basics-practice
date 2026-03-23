def log_decorator(func):
    def output_func():
        print(f"Вызвана функция {func.__name__}")
        func()
    return output_func

@log_decorator
def say_hello():
    print("Привет")

say_hello()

