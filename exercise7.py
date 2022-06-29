import pandas as pd
import numpy as np

def from_dict_and_labels(exam_data, labels):
    return pd.DataFrame(data=exam_data, index=labels)

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Number of attempts in the examination is greater than 2:

df = from_dict_and_labels(exam_data, labels)

print(df[df.attempts > 2])
print(df.loc[df.attempts > 2])