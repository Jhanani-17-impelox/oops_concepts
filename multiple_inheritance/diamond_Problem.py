# Problem 3: Demonstrating the Diamond Problem

# Create a class hierarchy like this:
# A has a method message()
# B and C inherit from A and override message()
# D inherits from both B and C
# Create an object of D and call message()
# Observe which method is called and explain why using MRO

class A:
    def message(self):
        print("Message from A")

class B(A):
    def message(self):
        print("Message from B")
        super().message()

class C(A):
    def message(self):
        print("Message from C")
        super().message()

class D(B, C):
    def message(self):
        print("Message from D")
        super().message()

# Create object of D
d = D()

# Call message()
print("Calling message():")
d.message()

# Print the Method Resolution Order
print("\nMethod Resolution Order (MRO) of class D:")
print(D.__mro__)