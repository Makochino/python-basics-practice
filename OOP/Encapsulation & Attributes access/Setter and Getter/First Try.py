class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def set_age(self, age):
        if 0 < age < 110:
            self.__age = age
        else:
            print("Недопустимый возраст")

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def print_person(self):
        print(f"Имя {self.__name}\tВозвраст {self.__age}")

tom = Person("Tom", 39)
tom.print_person()
tom.set_age(-3424242)
tom.set_age(25)
tom.print_person()