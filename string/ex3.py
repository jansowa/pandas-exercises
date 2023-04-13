import pandas as pd

df = pd.DataFrame({"col": [1, 12.13, 100.00]})
df["col"] = df["col"].astype(str).str.rjust(width=8, fillchar="0")

print(df)