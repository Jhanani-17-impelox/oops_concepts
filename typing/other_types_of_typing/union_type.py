# Union (multiple possible types)

from typing import Union

def square(x: Union[int, float]) -> float:
    return x * x

print(square(3))     # 9
print(square(2.5))   # 6.25
