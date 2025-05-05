# Problem 2: Animal → Mammal → Dog

# Create a multilevel class chain:
# Animal: Method: breathe()
# Mammal (inherits Animal): Method: feed_milk()
# Dog (inherits Mammal): Method: bark()
# Create object of Dog and call all three methods.

class Animal:
    def breathe(self):
        print("Breathing...")

class Mammal(Animal):
    def feed_milk(self):
        print("Feeding milk to young ones")

class Dog(Mammal):
    def bark(self):
        print("Woof! Woof!")

# Create a Dog object
my_dog = Dog()

# Call all three methods
print("Dog's activities:")
my_dog.breathe()     # From Animal class
my_dog.feed_milk()   # From Mammal class
my_dog.bark()        # From Dog class