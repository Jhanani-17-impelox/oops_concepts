def decorator(func):
    def wrapper(name):         # Accept the same args as original
        print("Start")
        func(name)
        print("End")
    return wrapper

@decorator
def say_hello(name):
    print("Hello", name)

say_hello("Jhanani")
