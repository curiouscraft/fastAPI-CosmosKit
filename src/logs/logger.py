import os, zipfile, uuid, logging
from logging.handlers import TimedRotatingFileHandler
from fastapi.logger import logger

logger.setLevel(logging.DEBUG)

# Create a file handler
fileHandler = TimedRotatingFileHandler("logs/app.log", backupCount=10, when='midnight', interval=1)
fileHandler.setLevel(logging.DEBUG)
fileHandler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
fileHandler.namer = lambda name: name.replace("app.log", "") + '_app.log'
logger.addHandler(fileHandler)

# Create a console handler
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)
consoleHandler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(consoleHandler)

# Disable propagation to avoid duplication of logs
logger.propagate = False
new_logger = logger