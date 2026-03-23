class Rectangle:

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def Rectangle_area(self):
        print(f"Площадь заданного прямоугольника = {self.width * self.length} см²")

    def Rectangle_perimeter(self):
        print(f"Периметр заданного прямоугольника = {2 *(self.width + self.length)} см")

number1 = Rectangle(15, 20)
number2 = Rectangle(10, 5)

number1.Rectangle_area()
number1.Rectangle_perimeter()

number2.Rectangle_area()
number2.Rectangle_perimeter()