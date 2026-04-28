from loguru import logger
from dotenv import load_dotenv
from sys import stderr
from os import getenv
load_dotenv()
def config_logger():
    logger.remove()
    logger.add(stderr, level=getenv("LOG_LEVEL", "INFO"))