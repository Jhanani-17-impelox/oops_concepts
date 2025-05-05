# Design an abstract class Vehicle with an abstract method move(). 
# Create subclasses like Car, Bike, and Truck where each subclass provides its own implementation of move(). 
# The Vehicle class should not define how the vehicle moves, but the subclasses should.

from abc import ABC, abstractmethod

# Abstract class Vehicle
class Vehicle(ABC):
    
    @abstractmethod
    def move(self):
        pass

# Subclass Car
class Car(Vehicle):
    
    def move(self):
        return "The car is driving on the road."

# Subclass Bike
class Bike(Vehicle):
    
    def move(self):
        return "The bike is pedaling on the road."

# Subclass Truck
class Truck(Vehicle):
    
    def move(self):
        return "The truck is hauling cargo on the highway."

# Testing the classes
def test_vehicles():
    vehicles = [Car(), Bike(), Truck()]
    
    for vehicle in vehicles:
        print(vehicle.move())

test_vehicles()
