def simple_decorator(func):                # Step 1: A decorator takes a function
    def wrapper():                         # Step 2: Wrapper adds extra work
        print("Before the function runs")  # Extra work before
        func()                             # Call the original function
        print("After the function runs")   # Extra work after
    return wrapper                         # Step 3: Return the wrapper

@simple_decorator                          # Step 4: Decorate the function
def my_func():
    print("This is the main function.")

my_func()
