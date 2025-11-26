import logging
logger = logging.getLogger(__name__)
logger.propagate = False#avoid propagating to the base logger
logger.info('hello from Logging')