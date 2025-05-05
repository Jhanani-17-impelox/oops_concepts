#Type Aliases:

from typing import List

Vector = List[float]

def total(v: Vector) -> float:
    return sum(v)

print(total([1.0, 2.5, 3.0]))  # 6.5
