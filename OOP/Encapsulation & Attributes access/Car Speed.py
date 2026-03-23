class Car:
    def __init__(self):
        self._mileage = 1000

    def driving(self, drive):
        if drive > 0:
            self._mileage += drive
            return f"The mileage increased by {drive}"
        else:
            return "The drive must be bigger that nothing(0 miles)!!!"
        
    def get_mileage(self):
        return f"The mileage: {self._mileage}"
    
lamborgini = Car()
print(lamborgini.driving(150))
print(lamborgini.get_mileage())