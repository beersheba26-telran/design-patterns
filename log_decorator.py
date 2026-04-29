from functools import wraps

from loguru import logger
def log(level:str):
    def log_inner(fn):
        @wraps(fn)
        def wrapper(*a, **k):
            logger.log(level,f"positional arguments {a}; keys arguments {k}")
            res = fn(*a, **k)
            logger.log(level, f"function {fn.__name__} returned result {res}")
            return res
        return wrapper
    return log_inner