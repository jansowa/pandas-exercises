import pandas as pd
import numpy as np

df = pd.DataFrame({"W": [68.0, 75.0, 86.0, 80.0, np.nan],
              "X": [78.0, 75.0, np.nan, 80.0, 86.0],
              "Y": [84, 94, 89, 86, 86],
              "Z": [86, 97, 96, 72, 83]})

s = pd.Series([68.0, 75.0, 86.0, 80.0, np.nan])

print(df.ne(s, axis=0))