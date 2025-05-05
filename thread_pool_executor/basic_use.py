"""  
How This Code Works:
- Creating a Thread Pool (ThreadPoolExecutor)
- The with ThreadPoolExecutor() as executor: statement creates a pool of worker threads.
- By default, it will use a number of threads equal to the CPU cores available.
- Submitting Tasks (submit())
- executor.submit(print_number, 10) submits the print_number(10) task to a worker thread.
- executor.submit(print_number, 20) submits the print_number(20) task to another worker thread.


- Parallel Execution Possibility:
- If enough threads are available, both tasks will execute concurrently.
- However, since print() is a simple operation, they may run almost instantly, and you might not notice the parallel behavior.
- The order of execution is not guaranteed because threads work independently.

"""




from concurrent.futures import ThreadPoolExecutor

def print_number(n):
    print("Number:", n)

with ThreadPoolExecutor() as executor:
    executor.submit(print_number, 10)
    executor.submit(print_number, 20)
