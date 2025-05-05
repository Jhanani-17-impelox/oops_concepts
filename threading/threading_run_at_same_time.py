import threading

def task1():
    for i in range(3):
        print("Task 1")

def task2():
    for i in range(3):
        print("Task 2")

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()  # Starts task1 in new thread
t2.start()  # Starts task2 in new thread

t1.join()   # Waits for task1 to finish
t2.join()   # Waits for task2 to finish

print("Both tasks finished")
