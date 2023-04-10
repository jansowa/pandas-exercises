import pandas as pd

s = pd.Series([1, 3, 5, 8, 10, 11, 15])
print(s.diff())
print(s.diff().diff())
