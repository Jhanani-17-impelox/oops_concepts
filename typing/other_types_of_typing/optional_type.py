from typing import Optional

def greet(name: Optional[str]) -> str:
    if name:
        return f"Hello, {name}"
    return "Hello, Guest"

print(greet("Jhanani"))  # Hello, Jhanani
print(greet(None))       # Hello, Guest
