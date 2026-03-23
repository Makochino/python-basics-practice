class Person:
    def __init__(self):
        self.__age = "16 y.o."

    def get_age(self):
        return self.__age
            
small_niger = Person()
print(small_niger.get_age())