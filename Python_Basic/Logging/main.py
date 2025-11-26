import logging
"""
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')
"""
#level=logging.DEBUG make it possible to display the debug level and above(the entire 5 levels)
# format='%(asctimes)s - %(name)s - %(levelnames)s - %(messages)s' :to specify the logs attributes
#datefmt='m/%d/%Y %H:%M:%S': month/day/Year/hour/minute/second


#logging levels
"""
logging.debug('this is a debug message')
logging.warning('this is a warning message')
logging.error('this is a error message')
logging.critical('this is a critical message')
logging.info('this is a info message')
"""
#these indicate the severity of the events
#warning,error,critical will be printed because by default only levels of messages with level warning of above are printed
#to change this,set the basic configuration after importing logging module

"""
import helper
"""
#this will create a hierarchy of loggers,starting at root logger and new loggers get added to this hierarchy
#they propagate messages up to the base logger

"""
#handler:
logger = logging.getLogger(__name__)

#create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file,log')

#level and the format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter(' %(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('warning')
logger.error('error')
"""
#define config
"""
import logging.config
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('simpleExample')
logger.debug('debug message')
"""
"""
#capturing stack traces
import traceback
try:
    a =[1,2,3]
    val =a[4]
except:
    logging.error("The error is %s",traceback.format_exc())
"""
"""
#rotating:
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#roll over after 2kb and keep back up logs app.log.1 app.log.2,etc
handler = RotatingFileHandler('app.log',maxBytes = 2000,backupCount=5)
logger.addHandler(handler)

for _ in range(10000):
    logger.info('hello world')

"""
#TimeRotating
import time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#s,m,h,d,midnight,w0
handler = TimedRotatingFileHandler('timed_test.log',when='s',interval=5,backupCount=5)
logger.addHandler(handler)

for _ in range(6):
    logger.info('Hello World')
    time.sleep(5)