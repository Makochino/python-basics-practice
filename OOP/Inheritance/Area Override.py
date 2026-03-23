import math

class Shape:
    def area(self):
          return 0
     
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return round(math.pi * self.radius**2)
        
    
class Rectangle(Shape): 
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self): 
        return self.width * self.height

shape = [Circle(5), Rectangle(10, 15)]

for shape in shape:
    print(f"{type(shape).__name__} area: {shape.area()}")