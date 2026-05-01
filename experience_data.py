from sortedcontainers import SortedDict
experience_wage_commissions = SortedDict({
    3:  (100, 0.001),   # up to 3 years
    5:  (110, 0.005),   # 3 up to 5 years
    8:  (130, 0.01),    # 5 up to 8 years
    10: (140, 0.015),   # 9 up to 10 years
    100: (200, 0.02),  # more than 10 years
})