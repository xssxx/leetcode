# 2023.12.02

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    out = employees.iloc[0:3, ]
    return out
    