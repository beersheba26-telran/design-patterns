from dataclasses import dataclass
from typing import Callable
@dataclass
class Employee:
    id: int
    name: str
    hire_date: str # ISO Date string yyyy-mm--dd
    basic_salary: int
    salary_stratagy: "SalaryStrategy"
@dataclass
class EmployeePayment:
    wage: float # cost of one hour
    hours: int # number of hours
    commisions: float # percent from sales
    sales: float # revenue from the sales
SalaryStrategy = Callable[[Employee, EmployeePayment], float]
def salaried(empl: Employee, payment: EmployeePayment) -> float:
    return empl.basic_salary
def hours(empl: Employee, payment: EmployeePayment) -> float:
    return salaried(empl, payment) + payment.hours * payment.wage
def sales(empl: Employee, payment: EmployeePayment) -> float: 
    return hours(empl, payment) + payment.commisions * sales
payment = EmployeePayment(150, 200, 0.01, 100000)
empl1: Employee = Employee(123, "Vasya", "2000-10-10", 10000,hours) 

print(empl1.salary_stratagy(empl1, payment))  



