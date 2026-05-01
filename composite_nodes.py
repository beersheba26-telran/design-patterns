from abc import ABC, abstractmethod
class Node(ABC):
    @abstractmethod
    def render(self) -> str: pass
class Text(Node):
    def __init__(self, text: str) :
        self.__text = text 
    def render(self) :
        return self.__text
class Group(Node):
    def __init__(self, *children: Node):
        self.__children = list(children) 
    def render(self)->str :
        return "".join(node.render() for node in self.__children)