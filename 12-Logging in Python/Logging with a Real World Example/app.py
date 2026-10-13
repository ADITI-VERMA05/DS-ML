import logging

## logging configuration settings
logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level to DEBUG
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Define the log message format
    datefmt='%Y-%m-%d %H:%M:%S',  # Define the date format
    handlers=[
        logging.FileHandler('app1.log'),  # Log to a file named 'app.log'
        logging.StreamHandler()  # Also log to the console
    ]
)

## create a logger object
logger = logging.getLogger("Arithematic_APP")

def add(a,b):
    result = a + b
    logger.debug(f"Adding {a} + {b} = {result}")
    return result

def subtract(a,b):
    result = a - b
    logger.debug(f"Subtracting {a} - {b} = {result}")
    return result

def multiply(a,b):
    result = a * b
    logger.debug(f"Multiplying {a} * {b} = {result}")
    return result

def divide(a,b):
    try:
        result = a / b
        logger.debug(f"Dividing {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Attempted to divide by zero")
        return None
    
## calling the functions to test logging
add(10, 5)
subtract(10, 5)
multiply(10, 5)
divide(10, 5)
divide(10, 0)  # This will log an error due to division by zero