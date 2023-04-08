import pandas as pd
import numpy as np

s = pd.Series(np.random.randint(0, 10, 40))
print(s.value_counts())