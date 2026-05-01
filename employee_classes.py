from dataclasses import dataclass
from typing import Callable
@dataclass
class Employee:
    id: int
    name: str
    hire_date: str # ISO Date string yyyy-mm--dd
    basic_salary: int
    salary_strategy: "SalaryStrategy"
@dataclass
class EmployeePayment:
    wage: float # cost of one hour
    hours: int # number of hours
    commisions: float # percent from sales
    sales: float # revenue from the sales
SalaryStrategy = Callable[[Employee, EmployeePayment], float]