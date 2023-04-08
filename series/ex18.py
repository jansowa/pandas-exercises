import pandas as pd
import numpy as np

s = pd.Series(np.random.uniform(0, 20, 20))
print([s.min(), s.quantile(0.25), s.median(), s.quantile(0.75), s.max()])
print(np.percentile(s, [0, 25, 50, 75, 100]))