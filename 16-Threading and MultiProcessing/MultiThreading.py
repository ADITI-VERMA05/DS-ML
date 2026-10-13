### Mutlithreading
### When to use Multi Threading
'''
1. I/O-bound tasks: Tasks that spen more time waiting for I/O operations (e.e., file operations, network requests).
2. Concurrent execution: When you want to improve the throughput of your application by allowing multiple tasks to run concurrently.
3. Responsiveness: Keeping the application responsive by offloading long-running tasks to background threads.
4. Resource sharing: When you need to share resources (like memory) between threads without the overhead of process-based concurrency.
5. Lightweight: Threads are generally lighter than processes, making them more efficient for certain tasks. 
6. Simplified communication: Threads can share memory space, making it easier to communicate between them compared to processes.
7. Real-time applications: When you need to handle real-time data processing or user interactions without blocking the main thread.
8. Parallelism: When you want to perform multiple operations simultaneously to speed up execution.
'''

import threading
import time
def print_numbers():
    for i in range(1, 6):
        time.sleep(2)  # Simulating a time-consuming task
        print(f"Number: {i}")
        
def print_letters():
    for letter in 'abcde':
        time.sleep(2)  # Simulating a time-consuming task
        print(f"Letter: {letter}")
        

## create 2 threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)
        
#stating time for the threads
t = time.time()

## start the thread
t1.start()  # print_numbers()
t2.start()  # print_letters()

## wait for the threads to complete
t1.join()
t2.join()

## print Time taken
finished_time = time.time() - t
print(f"Time taken: {finished_time}")


'''
Number: 1
Letter: a
Number: 2
Letter: b
Letter: c
Number: 3
Letter: d
Number: 4
Letter: e
Number: 5
Time taken: 10.008007764816284
'''