from functools import wraps
from lru_cache import LruCache

def cache(maxsize: int = 128):
    '''
    Least Recently Used cache decorator using LruCache class.
    maxsize - maximum number of cached results
    '''
    def cache_inner(fn):
        lru_cache = LruCache(maxsize)
        
        @wraps(fn)
        def wrapper(*args, **kwargs):
            # Create a hashable key from arguments
            key = (args, tuple(sorted(kwargs.items())))
            
            try:
                # Try to access from cache (marks as recently used)
                return lru_cache.access(key)
            except KeyError:
                # Not in cache - compute result
                result = fn(*args, **kwargs)
                # Add to cache (LruCache handles eviction automatically)
                lru_cache.add(key, result)
                return result
        
        return wrapper
    return cache_inner