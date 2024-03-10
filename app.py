from src.MLProject.logger import logging
from src.MLProject.exception import CustomException
import sys


if __name__=="__main__":
    logging.info("The execution has started")

try:
    a=1/0
except Exception as e:
    logging.info("Custom exception")
    raise CustomException(e,sys)
    
