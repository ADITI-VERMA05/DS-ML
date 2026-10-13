### MultiThreading with Thread Pool Executor

from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"Number: {number}"

numbers = [1,2,3,4,5]

#stating time for the threads
t = time.time()

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_number, numbers)
    
for result in results:
    print(result)

## print Time taken
finished_time = time.time() - t
print(f"Time taken: {finished_time}")

'''
Number: 1
Number: 2
Number: 3
Number: 4
Number: 5
Time taken: 1.004789113998413
'''