from loguru import logger
from logging_config import config_logger
from typing import Any
config_logger()
def variadic_fun(*args:Any):
    '''
    any number of arguments at a function call
    args - paramter dersignating tuple with arguments
    '''
    logger.info(args)

variadic_fun()  # no arguments - empty tuple
variadic_fun("abc", 10, [1, 2,3], ("a", 1))  