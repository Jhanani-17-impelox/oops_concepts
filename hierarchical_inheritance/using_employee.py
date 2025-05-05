
"""
Problem 2: Employee → Developer, Designer
Create classes:
Employee: Attributes: name, emp_id, method display_info()
Developer inherits Employee: Attribute programming_language, method code()
Designer inherits Employee: Attribute design_tool, method design()
Create objects of Developer and Designer and call all available methods
"""

class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
    
    def display_info(self):
        print(f"Employee {self.emp_id}: {self.name}")

class Developer(Employee):
    def __init__(self, name, emp_id, programming_language):
        super().__init__(name, emp_id)
        self.programming_language = programming_language
    
    def code(self):
        print(f"{self.name} is coding in {self.programming_language}")

class Designer(Employee):
    def __init__(self, name, emp_id, design_tool):
        super().__init__(name, emp_id)
        self.design_tool = design_tool
    
    def design(self):
        print(f"{self.name} is designing with {self.design_tool}")

# Problem 2 Demo
print("\nProblem 2: Employee Hierarchy")
dev = Developer("Alice", "D001", "Python")
designer = Designer("Bob", "D002", "Figma")

dev.display_info()
dev.code()

designer.display_info()
designer.design()
