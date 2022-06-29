import pandas as pd

def merge_two_series(s1, s2):
    return pd.concat([s1, s2], axis=1)

s1 = pd.Series([1, 2, 3, 4])
s2 = pd.Series([10, 20, 30, 40])

# print(pd.concat([s1, s2], axis=1))
print(merge_two_series(s1, s2))