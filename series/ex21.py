import pandas as pd
import numpy as np

s = pd.Series(range(31))
print(s[s % 5 == 0].index)
print(np.where(s % 5 == 0))
