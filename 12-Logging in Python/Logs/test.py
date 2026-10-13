from logger import logging

def add(a,b):
    logging.debug('Addition operation taking place')
    return a+b

logging.debug('Starting the addition function')
result = add(5, 10)