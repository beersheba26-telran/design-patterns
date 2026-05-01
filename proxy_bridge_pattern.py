from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Iterable
import json
@dataclass
class Employee:
    id: int
    name: str

class Company(ABC):
    @abstractmethod
    def addEmployee(self, empl:Employee): pass
    @abstractmethod
    def getEmployees(self) -> Iterable: pass 
#################################################       
class CompanySet(Company):
    __employees: set[Employee]
    def __init__(self):
        self.__employees = set()
    def addEmployee(self, empl: Employee) :
        self.__employees.add(empl) 
    def getEmployees(self):
        return list(self.__employees) 
#################################################
class NetworkProtocol(ABC):
    def send_receive(self, *args, **parameters) : pass
class HttpProtocol(NetworkProtocol):
    def __init__(self, baseURL: str):
        self.__baseUrl = baseUrl
    def send_receive(self, *arg, **parameters):
        '''
        sending HTTP request being created on basis parameters
        ''' 
class CompanyNetworkProxy(Company) :
    __protocol: NetworkProtocol
    def __init__(self, protocol: NetworkProtocol) :
        self.__protocol = protocol
    def addEmployee(self, empl:Employee) :
        self.__protocol.send_receive(empl)
    def getEmployees(self)->Iterable[Employee]:
        employeesJson = self.__protocol.send_receive()
        return json.load(employeesJson) 

employeesHttpProtocol: NetworkProtocol = HttpProtocol("https://tel-ran.org/employees")  

 
                    
