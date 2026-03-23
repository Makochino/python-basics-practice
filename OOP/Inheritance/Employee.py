class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def get_info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nId: {self.employee_id}")

emp = Employee("Maksim", 16, "gh3215b")
emp.get_info()