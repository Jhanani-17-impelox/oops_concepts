from concurrent.futures import ThreadPoolExecutor

def square(n):
    return n * n

with ThreadPoolExecutor() as executor:
    future1 = executor.submit(square, 2)
    future2 = executor.submit(square, 5)

    print("Result 1:", future1.result())  # Output: 4
    print("Result 2:", future2.result())  # Output: 25
    