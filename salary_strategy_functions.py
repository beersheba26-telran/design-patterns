from employee_classes import Employee, EmployeePayment


def salaried(empl: Employee, payment: EmployeePayment) -> float:
    return empl.basic_salary
def hours(empl: Employee, payment: EmployeePayment) -> float:
    return salaried(empl, payment) + payment.hours * payment.wage
def sales(empl: Employee, payment: EmployeePayment) -> float: 
    return hours(empl, payment) + payment.commisions * payment.sales