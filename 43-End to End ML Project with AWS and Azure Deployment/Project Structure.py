'''
—Agenda__
1. Project structure
2. logging
3. exception handling
4. utility file

»» in 'src' folder »»
>> create 'components' folder 
>> create 'pipeline' folder 
>> create 'exception.py'
>> create 'logger.py'  
>> create 'utils.py'  

» in components folder create
>> __init__.py 
>> data_ingestion.py
>> data_transformation.py
>> model_trainer.py
>> model_pusher.py [not now]

» in 'pipeline' folder create 
>> __init__.py 
>> train_pipeline.py
>> predict_pipeline.py

______exception.py______

import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message

_______logger.py______

import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

» python src/logger.py  >> log folder is created containing all log files


_____utils.py______
        
'''