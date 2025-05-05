#Callable Type (for functions as arguments)

from typing import Callable

def execute(func: Callable[[int, int], int]) -> int:
    return func(10, 5)

def add(a: int, b: int) -> int:
    return a + b

print(execute(add))  # 15
