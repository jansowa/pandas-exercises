import pandas as pd
import numpy as np


def from_dict_and_labels(exam_data, labels):
    return pd.DataFrame(data=exam_data, index=labels)


exam_data = {
    'name': ['Anastasia', 'Anastasia', 'Dima', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura',
             'Kevin', 'Jonas'],
    'score': [10, 12.5, 10, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 1, 1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'yes', 'yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', np.nan]}
labels = ['a0', 'a', 'b0', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = from_dict_and_labels(exam_data, labels)

def solution(df, column):
    df.loc[:, column] = df[column].replace("James", "Suresh")

def solution2(df, column):
    df.loc[:, column] = df[column].map(lambda val: "Suresh" if val == "James" else val)

solution(df, "name")
# solution2(df, "name")
print(df)
