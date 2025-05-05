#TypedDict (structured dict)

from typing import TypedDict

class Student(TypedDict):
    name: str
    age: int
    grade: str

def display(s: Student):
    print(f"{s['name']} is {s['age']} years old in grade {s['grade']}.")

display({"name": "Jhanani", "age": 21, "grade": "A"})