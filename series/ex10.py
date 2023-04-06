import pandas as pd

s = pd.Series([["Red", "Green", "White"], ["Red", "Black"], ["Yellow"]])
print(s.explode(ignore_index=True))
print(s.apply(pd.Series).stack().reset_index(drop=True))
