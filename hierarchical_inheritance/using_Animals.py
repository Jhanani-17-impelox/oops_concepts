"""
Problem 1: Animal → Dog, Cat
Create classes:
Animal: Method speak() prints "Animal speaks"
Dog inherits Animal: Override speak() to print "Dog barks"
Cat inherits Animal: Override speak() to print "Cat meows"
Create objects of Dog and Cat, call speak()
"""

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Problem 1 Demo
print("\nProblem 1: Animal Hierarchy")
dog = Dog()
cat = Cat()
dog.speak()  # Output: Dog barks
cat.speak()  # Output: Cat meows
