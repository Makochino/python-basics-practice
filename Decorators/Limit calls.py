import functools

def limit_calls(func):
    call_count = 0

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal call_count
        if call_count < 3:
            call_count += 1
            return func(*args, **kwargs)
        else:
            print("Функция вызвана слишком много раз!")

    return wrapper

@limit_calls
def test():
    print("Функция выполнена!")

test()
test()
test()
test()
test()

