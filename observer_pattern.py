from abc import ABC, abstractmethod
from loguru import logger
import weakref
class Subject(ABC):
    @abstractmethod
    def subscribe(self,observer: "Observer"): pass
    
    @abstractmethod
    def notify(self,message: str): pass
    @abstractmethod
    def message(self)-> str: pass
class Observer(ABC):
    @abstractmethod
    def update(self,subject: Subject):
        pass
class NewsAgency(Observer) :
    def __init__(self, name:str):
        self.__name = name
    def update(self, subject: Subject):
        logger.info(f"received {subject.message()} for {self.__name} agency")
         
class EmailNotification(Observer):
    def __init__(self, *emails:str):
        self.__emails = list(emails) 
    def update(self, subject: Subject):
        logger.info(f" {subject.message()} has been sent to {self.__emails}")  
class NewsPublisher(Subject):
    __observers: list[weakref.ReferenceType[Observer]]
    def __init__(self):
        self.__observers = [] #list of the weak references to observers
        self.__message = ""
    def subscribe(self,observer: Observer):
        self.__observers.append(weakref.ref(observer, lambda obs: self.__observers.remove(obs))) 
    def notify(self, message: str):
        self.__message = message 
        for observer_ref in self.__observers:
            observer_ref().update(self) 
    def message(self):
        return self.__message
                


