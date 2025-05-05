import threading
import time

class PrintMessageThread(threading.Thread):
    def __init__(self, name, message, delay):
        super().__init__()
        self.name = name  # Thread identifier
        self.message = message
        self.delay = delay
    
    def run(self):
        print(f"[{self.name}] Starting thread...")
        for i in range(3):
            print(f"[{self.name}] Iteration {i + 1}: {self.message}")
            time.sleep(self.delay)  # Simulating work
        print(f"[{self.name}] Finished execution.")

# Creating multiple threads with different messages and delays
thread1 = PrintMessageThread("Thread 1", "Processing...", 1)
thread2 = PrintMessageThread("Thread 2", "Running in parallel!", 2)
thread3 = PrintMessageThread("Thread 3", "Executing tasks...", 3)

# Start all threads
print("[Main] Starting all threads.")
thread1.start()
thread2.start()
thread3.start()

# Ensure all threads complete before main execution ends
thread1.join()
thread2.join()
thread3.join()

print("[Main] All threads completed. Main program execution finished.")