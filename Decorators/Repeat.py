import functools

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            count = 0
            while count != n:
                func()
                count += 1
        return wrapper
    return decorator

@repeat(5)
def hello():
    print("Привет!")

hello()
