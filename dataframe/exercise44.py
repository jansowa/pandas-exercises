import pandas as pd
import numpy as np

array = np.array([[1, 2], [3, 4]])
# print(array)

df = pd.DataFrame(array, columns=("col1", "col2"), index=("a", "b"))
print(df)