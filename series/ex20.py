import pandas as pd
import numpy as np

s = pd.Series(np.random.randint(0, 3, 15))
print(s)
print()
print(s.where(s==s.value_counts().index[0], "other"))
print()

s = pd.Series(np.random.randint(0, 3, 15))
print(s)
print()
s[s != s.value_counts().index[0]] = "other"
print(s)
