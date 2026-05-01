import weakref
from dataclasses import dataclass
@dataclass
class X:
    x:int

xs: list[X]  = [] #list of weak refereences

numbers: list[X] = [X(num) for num in range(10)] #list of strong references
a = numbers[0] #saving reference to X(0)
for num in numbers: #filling list of weak references
    xs.append(weakref.ref(num, lambda wr: xs.remove(wr)))
numbers.remove(X(0))
del a  
print([ref() for ref in xs]) #list of weak references won't contain reference to X(0)



