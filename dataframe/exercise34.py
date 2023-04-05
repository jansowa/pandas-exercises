import pandas as pd
import numpy as np

def from_dict_and_labels(exam_data, labels):
    return pd.DataFrame(data=exam_data, index=labels)

def replace_value(df, row_idx, column_idx, value):
    df.iloc[row_idx, column_idx] = value
    return df

def replace_value2(df, row_idx, column_name, value):
    df.at[row_idx, column_name] = value
    return df

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = from_dict_and_labels(exam_data, labels)

print(replace_value(df, 1, 2, "test"))
print(replace_value2(df, 1, "attempts", "test"))