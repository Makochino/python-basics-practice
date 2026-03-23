class Circle:
    pi = 3.14159  # This is a class attribute

    def __init__(self, radius):
        self.radius = radius

    # This is a class method
    @classmethod
    def from_diameter(cls, diameter):
        # cls is a reference to the Circle class
        print(f"Creating a Circle instance from diameter: {diameter}")
        radius = diameter / 2
        return cls(radius)  # This is an alternative constructor

    # This is an instance method
    def get_area(self):
        return self.pi * self.radius**2

# Use the class method to create a new instance
circle2 = Circle.from_diameter(10)

# Use the instance method on the new object
print(f"The area is: {circle2.get_area()}")
# Output: The area is: 78.53975
