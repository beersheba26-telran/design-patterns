# Write fnction computeSalaryBudget(see TODO comments in comute_salary_budget module)
## Takes following key parameters 
- Iterable of employees (employees=)<br>
- dictionary with keys as employee id and values as number of additional working hours in current month({123: 100, 50: 110,...}) If no specific id value exists in dictionary, zero should be implied (employeesHours=)
- sales value (sales=) - revenue from the sales in the current month
## Returns total salary budget for all employees
## Introduce in separate module following configuration (think of the data structure)
-  employee with experience up to 3 years - wage = 100, commissions = 0.001
-  employee with experience from 3 up to 5 years - wage = 110, commissions = 0.005
-  employee with experience from 5 up to 8 years - wage = 130, commissions = 0.01
-  employee with experience from 9 up to 10 years - wage = 140, commissions = 0.015
-  employee with experience more than 10 years - wage = 200, commissions = 0.02
# Write unit test cases for the described above function