def decorator(func):
    def wrapper(*args, **kwargs):
        print("Function is starting")
        result = func(*args, **kwargs)
        print("Function ended")
        return result
    return wrapper

@decorator
def add(a, b, c):
    print("Adding numbers")
    return a + b 

# print(add(5, 10))  # Output: Adding numbers \n Function ended \n 15
print(add(5, 10, 15))  # Output: Adding numbers \n Function ended \n 30