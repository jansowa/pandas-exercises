import pandas as pd
import numpy as np
from math import sqrt

s1 = pd.Series(range(1, 11))
s2 = pd.Series([11, 8, 7, 5, 6, 5, 3, 4, 7, 1])

print(sqrt(np.square(s1-s2).sum()))
print(np.linalg.norm(s1-s2))
