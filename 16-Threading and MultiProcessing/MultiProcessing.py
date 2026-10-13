### Multi processing : Processes that run in parallel
## CPU-Bound Tasks - Tasks that are heavy on CPU usage(eg. mathematical computation, data processing).
## Parallel execution - Multiple cores of the CPU

import multiprocessing
import time

def square_numbers():
    for i in range(1,6):
        time.sleep(1)
        print(f"Square: {i*i}")
        
def cube_numbers():
    for i in range(1,6):
        time.sleep(1.5)
        print(f"Cube: {i*i*i}")
        
## create Entry Point
if __name__ == "__main__":
     
    ## create 2 processes
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    ## stating time for the processes
    t = time.time()

    ## start the processes
    p1.start()
    p2.start()

    ## wait for the process to complete
    p1.join()
    p2.join()

    ## print Time taken
    finished_time = time.time() - t
    print(f"Time taken: {finished_time}")
    
    
    '''
Square: 1
Cube: 1
Square: 4
Cube: 8
Square: 9
Square: 16
Cube: 27
Square: 25
Cube: 64
Cube: 125
Time taken: 7.729840278625488
'''