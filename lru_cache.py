from collections import OrderedDict
from typing import Generic, TypeVar, Hashable
K = TypeVar("K", bound=Hashable)
V = TypeVar("V")
class LruCache(Generic[K, V]):
    __orderedDict: OrderedDict[K, V]
    __current: int
    __maxsize: int
    def __init__(self, maxsize: int):
        '''
        initialization of cache
        '''
        self.__orderedDict = OrderedDict()
        self.__current = 0
        self.__maxsize = maxsize
        
    def add(self,k: K, v: V):
        '''
        adds pair of key and value
        '''
        if k in self.__orderedDict:
            self.__orderedDict.move_to_end(k)
        else:
            if self.__current + 1 > self.__maxsize:
                self.__orderedDict.popitem(last=False)
            self.__current += 1
        self.__orderedDict[k] = v
    
        
        
    def clear(self) :
        '''
        clearing cache
        '''
        self.__orderedDict.clear()
        self.__current = 0
    def access (self, k: K)->V:
        '''
        getting value by key
        raising KeyError exception if no key exists
        '''
        res = self.__orderedDict[k]
        self.__orderedDict.move_to_end(k)
        return res
    def __getitem__(self, key):
        return self.access(key)
    def __setitem__(self, key, value):
        self.add(key, value)
    def __iter__(self):
        return iter(self.__orderedDict)    
           
        
            
        
    

