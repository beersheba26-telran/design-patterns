from loguru import logger
from logging_config import config_logger
from abc import ABC, abstractmethod
'''
migartion from legacy interface to a new one
'''


#####################################
# leagacy interface and implementation
class LegacyLogger(ABC):
    @abstractmethod
    def print_message(self, message: str):
        pass

class RegularPrint(LegacyLogger): 
    def print_message(self, message: str) :
        logger.debug(f"method print from legacy logger is called with message {message}")
        print(message) 
#########################################
# new interface and adapter pattern implementation
class NewLogger(ABC):
    @abstractmethod
    def info(self, message: str) :
        pass 
class AdapterLogger(NewLogger) :
    def __init__(self,legacyLogger: LegacyLogger) :
        self.__legacyLogger = legacyLogger 
    def info(self, message: str) :
        self.__legacyLogger.print_message(message) 
###################################################
adapterLogger = AdapterLogger(RegularPrint())
adapterLogger.info("kuku")
               