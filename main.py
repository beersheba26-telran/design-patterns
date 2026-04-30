from cache_decorator import cache
from timing_decorator import timing

funObj = timing(1000)(sum)
funObj(range(1_000_000))

