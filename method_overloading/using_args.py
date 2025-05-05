#calculate the area of circle, square and rectangle using method overloading using args

import math
def Area(*args):
    if len(args) == 1:  # Circle
        r = args[0]
        area = math.pi * r * r
    elif len(args) == 2:  # Rectangle
        l, b = args
        area = l * b
    elif len(args) == 3:  # square
        s = args[0]
        area = s * s
    else:
        print("please enter valid number of values")


    return area

print(Area(5))  # Circle 
print(Area(5, 10))  # Rectangle 
print(Area(5, 5, 5))  # Square 
# print(Area(5, 10, 15,20))  #enterinf many number of arguements

