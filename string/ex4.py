import pandas as pd

df = pd.DataFrame({"col": ["abc", "de", "fbabfeaef"]})
df["col"] = df["col"].str.rjust(width=10, fillchar="0")

print(df)