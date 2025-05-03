# 2023.12.07

import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
  res = teacher.groupby('teacher_id').apply(lambda x: x.nunique()).drop(columns=['dept_id', 'teacher_id']).reset_index().rename(columns={'subject_id': 'cnt'})
  return res
    