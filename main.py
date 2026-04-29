from loguru import logger
from logging_config import config_logger
from time import perf_counter
from log_decorator import log
from timing_decorator import timing
config_logger()
@log(level="DEBUG")
@timing(100)
def arithmetic_progression(length: int):
    '''
    computes arithmetic progression sum of a given length
    '''
    
    return sum(range(length)) 

print(arithmetic_progression(1_000_000))
logger.info(arithmetic_progression.__doc__)

