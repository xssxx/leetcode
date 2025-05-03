# 2023.12.02

import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees.loc[:, 'salary'] *= 2
    return employees

    