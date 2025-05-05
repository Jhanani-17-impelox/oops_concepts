

class Employee:
    def __init__(self, name):
        self.name = name

    def get_role(self):
        return "Employee"


class Developer(Employee):
    def __init__(self, name):
        super().__init__(name)  

    def get_role(self):
        return f"{self.name} is a Developer"

    def describe(self):
        base_role = super().get_role()
        current_role = self.get_role()
        print(f"Base Role: {base_role}")
        print(f"Current Role: {current_role}")

d = Developer("Alice")
d.describe()
