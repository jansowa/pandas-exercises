import pandas as pd
import numpy as np

s = pd.Series(np.random.uniform(0, 10, 15))

print([s.autocorr(i) for i in range(14)])