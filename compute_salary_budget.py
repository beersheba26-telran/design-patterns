from typing import Iterable
from loguru import logger   
from employee_classes import Employee, EmployeePayment
from experience_data import experience_wage_commissions #TODO should be used to get the payment details for each employee for the current month

from datetime import date

def _get_experience_years(hire_date: str) -> int:
    hired = date.fromisoformat(hire_date)   # parses "yyyy-mm-dd"
    today = date.today()
    years = today.year - hired.year
    # Subtract 1 if the anniversary hasn't occurred yet this year
    if (today.month, today.day) < (hired.month, hired.day):
        years -= 1
    return years

def _get_payment_details(employee: Employee, hours, sales: float) -> EmployeePayment:
    experience_years = _get_experience_years(employee.hire_date)
    wage, commission = experience_wage_commissions[experience_years]
    payment_details = EmployeePayment(wage, hours, commisions=commission, sales=sales)
    return payment_details
    

def _employee_salary(employee: Employee, hours: int, sales: int) -> float:
    '''Computes the salary for a single employee according to their salary strategy and payment details'''
    res = employee.basic_salary  # default to basic salary if strategy fails
    logger.debug(f"Computing salary for employee {employee} with hours={hours} and sales={sales}")
    try:
        res = employee.salary_strategy(employee, _get_payment_details(employee, hours, sales))
        logger.debug(f"Computed salary for employee {employee}: {res}")
        
    except TypeError :
        logger.error(f"strategy function {employee.salary_strategy} doesn't exist or is not compatible to strategy function signature")
        logger.warning(f"Falling back to basic salary for employee {employee.id}")
    return res
def computeSalaryBudget(*, employees: Iterable[Employee], employeesHours: dict[int, int], sales: float) -> float:
    '''Computes the total salary budget for all employees
    according to their salary strategy and payment details
    received from experience based data and the current month sales, hours worked 
    '''
    total_budget = 0.0
    for employee in employees:
        total_budget += _employee_salary(employee,  employeesHours.get(employee.id, 0), sales)
    
    return total_budget