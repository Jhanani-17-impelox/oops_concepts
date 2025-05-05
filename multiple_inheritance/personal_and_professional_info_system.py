# Problem 1: Personal and Professional Info System
# Create classes Person, Employee, and Student.
# Person has name and age.
# Employee has employee_id and designation.
# Student has student_id and course.
# Create a class WorkingStudent that inherits from both Employee and Student.
# Implement a method to display all details from all three classes.

class Person:
    def __init__(self, name, age, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.age = age
    
    def get_person_details(self):
        return f"Name: {self.name}, Age: {self.age}"

class Employee:
    def __init__(self, employee_id, designation, **kwargs):
        super().__init__(**kwargs)
        self.employee_id = employee_id
        self.designation = designation
    
    def get_employee_details(self):
        return f"Employee ID: {self.employee_id}, Designation: {self.designation}"

class Student:
    def __init__(self, student_id, course, **kwargs):
        super().__init__(**kwargs)
        self.student_id = student_id
        self.course = course
    
    def get_student_details(self):
        return f"Student ID: {self.student_id}, Course: {self.course}"

class WorkingStudent(Employee, Student, Person):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def display_all_details(self):
        print("Working Student Details:")
        print(self.get_person_details())
        print(self.get_employee_details())
        print(self.get_student_details())

# Creating objects of each class
print("--- Person Object ---")
person = Person(name="Alice", age=30)
print(person.get_person_details())

print("\n--- Employee Object ---")
employee = Employee(employee_id="E100", designation="Manager")
print(employee.get_employee_details())

print("\n--- Student Object ---")
student = Student(student_id="S200", course="Computer Science")
print(student.get_student_details())

print("\n--- WorkingStudent Object ---")
working_student = WorkingStudent(
    name="Bob",
    age=25,
    employee_id="E300",
    designation="Teaching Assistant",
    student_id="S300",
    course="Mathematics"
)
working_student.display_all_details()