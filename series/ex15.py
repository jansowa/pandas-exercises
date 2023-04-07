import pandas as pd

s = pd.concat([pd.Series(range(1, 10)), pd.Series([5, 3])], ignore_index=True)
print("Mean: ", s.mean())
print("Standard deviation: ", s.std())