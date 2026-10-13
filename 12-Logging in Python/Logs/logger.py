## configuration logging
import logging

logging.basicConfig(
    filename='app.log',  # Log messages will be written to this file
    filemode='w',        # 'w' for overwrite, 'a' for append
    level=logging.DEBUG, # Set the logging level
    format='%(asctime)s- %(name)s - %(levelname)s - %(message)s',  # Log message format
    datefmt='%Y-%m-%d %H:%M:%S'  # Date format in log messages
)
