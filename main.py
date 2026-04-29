from loguru import logger
from logging_config import config_logger
from typing import Any
config_logger()
def key_fun(**empl):
    '''
    empl parameter disgnates dict
    at function call, key argiments shoyld be passed
    '''
    logger.debug(empl)
    
key_fun() 
key_fun(id=1, name="Vasya")   