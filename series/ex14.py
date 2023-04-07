import pandas as pd

s = pd.Series(range(1, 6))
s.index = ['A', 'B', 'C', 'D', 'E']
# s[[0, 1]] = s[[1, 0]]
print(s.loc[['B', 'A', 'C', 'D', 'E']])
print(s.reindex(['B', 'A', 'C', 'D', 'E']))