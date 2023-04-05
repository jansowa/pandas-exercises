import pandas as pd
import numpy as np


def from_dict_and_labels(exam_data, labels):
    return pd.DataFrame(data=exam_data, index=labels)


def specific_columns(df, columns):
    return df[columns]


def specific_columns2(df, columns):
    return df.loc[:, columns]


exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = from_dict_and_labels(exam_data, labels)
columns = ["score", "name"]

print(specific_columns(df, columns))
print(specific_columns2(df, columns))
