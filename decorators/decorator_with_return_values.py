def square_decorator(func):
    def wrapper(x):
        result = func(x)
        return result * result
    return wrapper

@square_decorator
def get_number(x):
    return x

print(get_number(5))  # Output: 25
