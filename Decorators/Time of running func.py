import time

def time_counter(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func()
        end = time.time()
        print(f"Fucntion with name({func.__name__}) was performed in {end - start:.4f} seconds")
    return wrapper

@time_counter
def func_instance():
    for _ in range(10**6):
        print(_)

func_instance()