# Create a base class Shape with an abstract method area(). 
# Then, create subclasses Circle and Rectangle that implement the area() method. 
# Ensure that the base class does not provide a concrete implementation of area().

from abc import ABC, abstractmethod
import math

# Base class Shape (abstract class)
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass  # No implementation, subclasses must define it

# Circle subclass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2  # Area of a circle

# Rectangle subclass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height  # Area of a rectangle

# Example Usage:
circle = Circle(5)  # Circle with radius 5
rectangle = Rectangle(4, 6)  # Rectangle with width 4 and height 6

print(f"Circle area: {circle.area()}")  # Should print the area of the circle
print(f"Rectangle area: {rectangle.area()}")  # Should print the area of the rectangle

