import logging
logger = logging.getLogger(__name__)
#__name__:global variable,this will create a logger with the name of the module where logs will be written in
logger.propagate = False#to avoid the propagation
logger.info('I am from helper')