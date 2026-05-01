from typing import Iterable

from employee_classes import Employee, EmployeePayment
from experience_data import experience_wage_commissions #TODO should be used to get the payment details for each employee for the current month

def computeSalaryBudget(*, employees: Iterable[Employee], employeesHours: dict[int, int], sales: float) -> float:
    '''Computes the total salary budget for all employees
    according to their salary strategy and payment details
    received from experience based data and the current month sales, hours worked 
    '''
    #TODO