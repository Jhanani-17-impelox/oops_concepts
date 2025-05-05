#  Use of super() in Multiple Inheritance
# Problem 4: Shape Area Calculator
# 
# Create classes:
# Shape with color attribute and describe() method
# Rectangle inherits from Shape and has length, breadth, and area()
# Triangle inherits from Shape and has base, height, and area()
# MultiShape inherits from both Rectangle and Triangle
# Use super() to call the parent class constructors and describe() methods
# Print area from both parent shapes

class Shape:
    def __init__(self, color, **kwargs):
        super().__init__(**kwargs)  # Important for multiple inheritance
        self.color = color
    
    def describe(self):
        print(f"I am a {self.color} shape")

class Rectangle(Shape):
    def __init__(self, length, breadth, **kwargs):
        super().__init__(**kwargs)
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth
    
    def describe(self):
        super().describe()
        print(f"I am a rectangle with length {self.length} and breadth {self.breadth}")

class Triangle(Shape):
    def __init__(self, base, height, **kwargs):
        super().__init__(**kwargs)
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height
    
    def describe(self):
        super().describe()
        print(f"I am a triangle with base {self.base} and height {self.height}")

class MultiShape(Rectangle, Triangle):
    def __init__(self, color, length, breadth, base, height):
        super().__init__(
            color=color,
            length=length,
            breadth=breadth,
            base=base,
            height=height
        )
    
    def describe(self):
        super().describe()
        print("I am a MultiShape that combines both rectangle and triangle")
    
    def show_areas(self):
        print(f"Rectangle area: {self.area()}")  # Calls Rectangle's area()
        # To call Triangle's area specifically:
        print(f"Triangle area: {Triangle.area(self)}")

# Create a MultiShape object
multi = MultiShape(
    color="blue",
    length=4,
    breadth=5,
    base=6,
    height=7
)

# Demonstrate functionality
print("=== Description ===")
multi.describe()

print("\n=== Areas ===")
multi.show_areas()

print("\n=== Method Resolution Order ===")
print(MultiShape.__mro__)