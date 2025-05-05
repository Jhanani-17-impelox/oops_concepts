# Problem 4: Shape → Polygon → Rectangle

# Create classes:

# Shape: Method: describe() → print "This is a shape"
# Polygon (inherits Shape): Method: describe() → print "This is a polygon"
# Rectangle (inherits Polygon): Method: describe() → print "This is a rectangle"
# Create object of Rectangle and observe method overriding (test using describe())

class Shape:
    def describe(self):
        print("This is a shape")

class Polygon(Shape):
    def describe(self):
        print("This is a polygon")

class Rectangle(Polygon):
    def describe(self):
        print("This is a rectangle")

# Create a Rectangle object
rect = Rectangle()

# Call describe() to observe method overriding
print("Calling describe():")
rect.describe()