# Problem 3: Person → Employee → Manager

# Build a class hierarchy:

# Person: Attributes: name, age
# Employee (inherits Person): Attributes: emp_id, department
# Manager (inherits Employee): Attribute: team_size
# Method in Manager to print all attributes using constructor chaining (super())

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, emp_id, department):
        super().__init__(name, age)  # Initialize Person attributes
        self.emp_id = emp_id
        self.department = department

class Manager(Employee):
    def __init__(self, name, age, emp_id, department, team_size):
        super().__init__(name, age, emp_id, department)  # Initialize Employee attributes
        self.team_size = team_size

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Department: {self.department}")
        print(f"Team Size: {self.team_size}")

# Create a Manager object
manager = Manager(
    name="Alice Johnson",
    age=35,
    emp_id="MGR101",
    department="Engineering",
    team_size=8
)

# Print all attributes
print("Manager Details:")
manager.display_details()