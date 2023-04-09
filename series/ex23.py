import pandas as pd

s1 = pd.Series(range(1, 11))
s2 = pd.Series([1, 3, 5, 7, 10])

print(s1[s1.isin(s2)].index)
print([pd.Index(s1).get_loc(i) for i in s2])