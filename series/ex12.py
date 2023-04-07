import pandas as pd

s1 = pd.Series([100, 200, "python", 300.12, 400])
s2 = pd.Series([500, "php"])

print(s1._append(s2))

print(pd.concat((s1, s2), ignore_index=True))