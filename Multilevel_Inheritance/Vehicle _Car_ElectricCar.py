# 🔹 Problem Statements for Multilevel Inheritance

# Problem 1: Vehicle → Car → ElectricCar

# Create a three-level inheritance structure:
# Vehicle: Attributes: make, model
# Car (inherits Vehicle): Attribute: fuel_type, Method: show_details()
# ElectricCar (inherits Car): Attribute: battery_capacity, Method: show_details() (override and include all info)
# Create an object of ElectricCar and call show_details() to display all inherited and current class details.

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def display_basic_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type
    
    def show_details(self):
        self.display_basic_info()
        print(f"Fuel Type: {self.fuel_type}")

class ElectricCar(Car):
    def __init__(self, make, model, fuel_type, battery_capacity):
        super().__init__(make, model, fuel_type)
        self.battery_capacity = battery_capacity  # in kWh
    
    def show_details(self):
        super().show_details()  # Calls Car's show_details() which includes Vehicle info
        print(f"Battery Capacity: {self.battery_capacity} kWh")

# Create an ElectricCar object
tesla = ElectricCar(
    make="Tesla",
    model="Model S",
    fuel_type="Electric",
    battery_capacity=100
)

# Call show_details() to display all information
print("Electric Car Details:")
tesla.show_details()