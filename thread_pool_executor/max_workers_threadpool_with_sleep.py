from concurrent.futures import ThreadPoolExecutor
import time

def task(n):
    print("Sleeping for", n, "seconds")
    time.sleep(n)
    return n

with ThreadPoolExecutor(max_workers=2) as executor:
    results = executor.map(task, [2, 3, 1, 4])

for r in results:
    print("Finished sleeping for", r, "seconds")
