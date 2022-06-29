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

def divide_by_ratio(df, ratio):
    split_row_number = int(df.shape[0]*ratio)
    return df[:split_row_number], df[split_row_number:]

def divide_by_raio_without_order(df, ratio):
    df1 = df.sample(frac=ratio)
    df2 = df.drop(df1.index)
    return df1, df2

df1, df2 = divide_by_ratio(df, 0.3)

print(df1)
print(df2)

df1, df2 = divide_by_raio_without_order(df, 0.3)
print(df1)
print(df2)