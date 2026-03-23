x = 5

def outer():
    x = 10  
    def change_x():
        nonlocal x
        x += 1  
        print("Inside change_x:", x)

    change_x()
    print("Inside outer:", x)

outer()
print("Global x:", x)
