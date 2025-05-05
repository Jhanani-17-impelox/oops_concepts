
"""
Problem 3: Shape → Circle, Square
Create hierarchy:
Shape: Method area() raises NotImplementedError
Circle inherits Shape: Implements area() using radius
Square inherits Shape: Implements area() using side length
Create object of each and calculate area
"""

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

# Problem 3 Demo
print("\nProblem 3: Shape Hierarchy")
circle = Circle(5)
square = Square(4)

print(f"Circle area: {circle.area():.2f}")  # Output: 78.54
print(f"Square area: {square.area()}")      # Output: 16