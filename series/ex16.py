import pandas as pd

s1 = pd.Series(range(1, 6))
s2 = pd.Series(range(2, 11, 2))
print(s1[~s1.isin(s2)])
