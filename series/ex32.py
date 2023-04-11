import pandas as pd
import numpy as np

s = pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1])

diffs = s.diff()
reversed_diffs = s.iloc[::-1].diff()[::-1]
print([i for i in s.index if diffs[i] > 0 and reversed_diffs[i] > 0])

temp = np.diff(np.sign(np.diff(s)))
result = np.where(temp == -2)[0] + 1
print(result)