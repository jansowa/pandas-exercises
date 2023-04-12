import pandas as pd

s1 = pd.Series([1, 3, 2, 4, 5])
s2 = pd.Series(range(1, 6))

print(s1 == s2)