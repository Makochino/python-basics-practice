class Vehicle:
    def __init__(self,  brand):
        self.brand = brand

    def drive(self):
        print("Driving a vehicle")

class Car(Vehicle):
    
    def drive(self):
        print("Driving a car")