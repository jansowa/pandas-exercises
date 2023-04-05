import pandas as pd
import numpy as np

def from_dict_and_labels(exam_data, labels):
    return pd.DataFrame(data=exam_data, index=labels)

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

df = from_dict_and_labels(exam_data, labels)

def drop_rows_by_index(df, index_list):
    return df.drop(index_list)

def drop_rows_by_number(df, row_number_list):
    return df.drop(df.index[row_number_list].values)

print(drop_rows_by_index(df, ['a', 'c']))
print(drop_rows_by_number(df, [2, 4]))