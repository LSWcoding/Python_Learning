import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctimes)s - %(name)s - %(levelnames)s - %(messages)s',
                     datefmt='m/%d/%Y %H:%M:%S')

#logging levels
logging.debug('this is a debug message')
logging.warning('this is a warning message')
logging.error('this is a error message')
logging.critical('this is a critical message')
logging.info('this is a info message')
#these indicate the severity of the events
#warning,error,critical will be printed because by default only levels of messages with level warning of above are printed
#to change this,set the basic configuration after importing logging module
import own_logger
#a hierarchy of logger is created,new loggers like own_logger get added to this hierarchy
#new loggers propagate the messages up to the base logger

#handler
logger =logging.getLogger(__name__)

#create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

#level and format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter(' %(name)s - %(levelnames)s - %(messages)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('this is a warning')
logger.error('this is a error')

#capturing stack traces
import traceback
try:
    a= [1,2,3]
    val = a[4]
except: 
    logging.error('this error is %s',traceback.format_exc())#this will print message to the log

#rotating
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = RotatingFileHandler('app.log',maxBytes= 2000,backupCount= 5)
logger.addHandler(handler)


for _ in range(10000):
    logger.info('Hello')