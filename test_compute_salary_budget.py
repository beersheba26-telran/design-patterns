from unittest import TestCase

from employee_classes import Employee
from salary_strategy_functions import salaried, hours, sales 
from compute_salary_budget import computeSalaryBudget


def _wrong_strategy():
    """Incompatible strategy with no parameters — will raise TypeError"""
    return 999.0


def _make_employee(hire_date: str, strategy=salaried, basic_salary=5000, emp_id=1):
    return Employee(id=emp_id, name="Test User", hire_date=hire_date, basic_salary=basic_salary, salary_strategy=strategy)


class TestComputeSalaryBudget(TestCase):

    def test_single_salaried_employee(self):
        # 3 years experience → wage=100, commission=0.001; salaried ignores payment
        emp = _make_employee("2023-05-01", strategy=salaried, basic_salary=3000)
        result = computeSalaryBudget(
            employees=[emp],
            employeesHours={1: 160},
            sales=0.0,
        )
        self.assertAlmostEqual(result, 3000.0)

    def test_multiple_employees_summed(self):
        # Both salaried — payment details irrelevant
        emp1 = _make_employee("2023-04-30", strategy=salaried, basic_salary=3000, emp_id=1)
        emp2 = _make_employee("2018-05-01", strategy=salaried, basic_salary=2000, emp_id=2)
        result = computeSalaryBudget(
            employees=[emp1, emp2],
            employeesHours={1: 160, 2: 160},
            sales=0.0,
        )
        self.assertAlmostEqual(result, 5000.0)

    def test_missing_hours_defaults_to_zero(self):
        # 5 years experience → wage=110; hours strategy: basic_salary + 0 * 110 = 2000
        emp = _make_employee("2021-04-30", strategy=hours, basic_salary=2000, emp_id=1)
        result = computeSalaryBudget(
            employees=[emp],
            employeesHours={},   # no hours recorded
            sales=0.0,
        )
        self.assertAlmostEqual(result, 2000.0)

    def test_hours_strategy_adds_wage_per_hour(self):
        # 8 years experience → wage=130; hours strategy: basic_salary + hours * wage
        emp = _make_employee("2018-05-01", strategy=hours, basic_salary=1000, emp_id=1)
        result = computeSalaryBudget(
            employees=[emp],
            employeesHours={1: 10},
            sales=0.0,
        )
        self.assertAlmostEqual(result, 1000 + 10 * 130.0)

    def test_sales_strategy_adds_commission(self):
        # 10 years experience → wage=140, commission=0.015
        emp = _make_employee("2016-05-01", strategy=sales, basic_salary=1000, emp_id=1)
        result = computeSalaryBudget(
            employees=[emp],
            employeesHours={1: 10},
            sales=20000.0,
        )
        self.assertAlmostEqual(result, 1000 + 10 * 140.0 + 0.015 * 20000.0)

    def test_empty_employee_list(self):
        result = computeSalaryBudget(employees=[], employeesHours={}, sales=0.0)
        self.assertEqual(result, 0.0)

    def test_wrong_salary_strategy_falls_back_to_basic_salary(self):
        # Wrong strategy with incompatible signature raises TypeError
        # Expected: fallback to basic_salary
        emp = _make_employee("2023-05-01", strategy=_wrong_strategy, basic_salary=2500, emp_id=1)
        result = computeSalaryBudget(
            employees=[emp],
            employeesHours={1: 160},
            sales=1000000,
        )
        self.assertAlmostEqual(result, 2500.0)



