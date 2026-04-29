from functools import wraps
from time import perf_counter
def timing(iterations: int=1):
    '''
    iterations - number of running iterations for measuring short operations
    '''
    def timing_inner(fn):
        @wraps(fn)
        def wrapper(*a, **k):
            start = perf_counter()
            for _ in range(iterations):
                res = fn(*a, **k)
            print(f"running time of function {fn.__name__} for {iterations} iterations is {(perf_counter() - start):.3f}") 
            return res 
        return wrapper
    return timing_inner  
    