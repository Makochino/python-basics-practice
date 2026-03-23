class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value_of_name):
        self.__name = value_of_name

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, yo):
        if 0 < yo < 100:
            self.__age = yo
        else:
            print("Age cannot be negative!!!")

man = Person("Maksim", 16)
print(man.name)
man.name = "Albert"
print(man.name)
