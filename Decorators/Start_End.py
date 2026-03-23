def start_end(func):
    def wrapper(*args, **kwargs):
        print("Function started")
        func()
        print("Function ended")
    return wrapper

@start_end
def just_func():
    print("Function working")

just_func()