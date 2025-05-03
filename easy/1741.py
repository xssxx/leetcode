# 2023.12.07

import pandas as pd

def total_time(df: pd.DataFrame) -> pd.DataFrame:
    new = df.groupby(['event_day', 'emp_id'])[['out_time', 'in_time']].sum()
    new['total_time'] = new['out_time'] - new['in_time']
    result = new.drop(columns=['in_time', 'out_time']).reset_index().rename(columns={'event_day': 'day'})
    return result
    