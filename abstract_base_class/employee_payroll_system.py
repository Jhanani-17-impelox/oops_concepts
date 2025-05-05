# Design an abstract base class Employee with an abstract method calculate_salary(). 
# Create subclasses FullTimeEmployee and PartTimeEmployee, where each subclass provides its own salary calculation logic. 
# Ensure that the common payroll interface is defined in the abstract base class.

from abc import ABC, abstractmethod

# Abstract Base Class for Employee
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

# Subclass for Full-Time Employee
class FullTimeEmployee(Employee):
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    
    def calculate_salary(self):
        # Full-time employee salary is just the base salary
        return self.base_salary

# Subclass for Part-Time Employee
class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    
    def calculate_salary(self):
        # Part-time employee salary is based on hourly rate and hours worked
        return self.hourly_rate * self.hours_worked


# Full-Time Employee
ft_employee = FullTimeEmployee("Jhanani", 50000)
print(f"Full-Time Employee Salary: {ft_employee.calculate_salary()}")

# Part-Time Employee
pt_employee = PartTimeEmployee("Jans", 20, 80)  # 80 hours worked at $20/hour
print(f"Part-Time Employee Salary: {pt_employee.calculate_salary()}")
