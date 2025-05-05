# Problem 2: Multiple Inheritance with Overridden Methods
# Create classes A, B, and C.
# Class A has a method show().
# Class B also has a method show().
# Class C inherits from both A and B and also has a show() method.
# Create an object of C and call show().
# Print the MRO of class C.


class A:
    def show(self):
        print("A's show()")

class B:
    def show(self):
        print("B's show()")

class C(A, B):
    def show(self):
        print("C's show()")
        super().show()  # This will call the next method in MRO

# Create object of C
obj = C()

# Call show() - this will demonstrate MRO in action
print("Calling show():")
obj.show()

# Print the Method Resolution Order
print("\nMethod Resolution Order (MRO) of class C:")
print(C.__mro__)