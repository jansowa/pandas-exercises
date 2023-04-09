import pandas as pd
import numpy as np

s = pd.Series(np.random.randint(0, 10, 5))
s.index = ['A', 'B', 'C', 'D', 'E']
print(s)

positions = [0, 2, 3]
print(s[positions])
print(s.iloc[positions])
print(s.take(positions))