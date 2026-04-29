from loguru import logger
from logging_config import config_logger
from typing import Any
config_logger()
def universal_fun(*args, **keys):
    '''
    empl parameter disgnates dict
    at function call, key argiments shoyld be passed
    '''
    logger.debug(keys) # logging dict with key arguments
    logger.debug(args) # logging tuple with positional arguments
    logger.info("".join("_" for _ in range(50)))
    
universal_fun() 
universal_fun(id=1, name="Vasya")   
universal_fun(1)
universal_fun(1, id=1, name="Vasya")