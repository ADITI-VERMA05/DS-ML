### MultiProcessing with Thread Pool Executor

from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
    time.sleep(1)
    return f"Square: {number * number}"

numbers = [1,2,3,4,5] 

## create Entry Point
if __name__ == "__main__":
    
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_number, numbers)
    
    #stating time for the threads
    t = time.time()
    
    for result in results:
        print(result)

    ## print Time taken
    finished_time = time.time() - t
    print(f"Time taken: {finished_time}")


'''
Square: 1
Square: 4
Square: 9
Square: 16
Square: 25
Time taken: 0.0009946823120117188
'''