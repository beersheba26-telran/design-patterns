from cache_decorator import cache
from timing_decorator import timing

@timing(1)
@cache(maxsize=3)
def arithmetic_progression(length: int):
    return sum(range(length))

arithmetic_progression(50_000_000)
arithmetic_progression(50_000_000)
arithmetic_progression(10_000_000)
arithmetic_progression(10_000_000)
arithmetic_progression(60_000_000)
arithmetic_progression(60_000_000)
arithmetic_progression(70_000_000)
arithmetic_progression(70_000_000)
arithmetic_progression(50_000_000)
arithmetic_progression(50_000_000)

