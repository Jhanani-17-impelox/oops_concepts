#Any Type (completely flexible)

from typing import Any

def print_data(data: Any):
    print(data)

print_data(10)         # 10
print_data("Jhanani")  # Jhanani
print_data([1, 2, 3])  # [1, 2, 3]
