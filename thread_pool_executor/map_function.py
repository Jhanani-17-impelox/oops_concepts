import threading
import time
from concurrent.futures import ThreadPoolExecutor

def square(n):
    print(f"Thread {threading.current_thread().name} is computing square of {n}")
    time.sleep(1)  # Simulating work delay
    return n * n

numbers = [1, 2, 3, 4]

with ThreadPoolExecutor() as executor:
    results = executor.map(square, numbers)  # Parallel execution

print("\nFinal Results:")
for r in results:
    print("Square is:", r)