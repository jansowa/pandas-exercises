import pandas as pd

df = pd.DataFrame({"col1" : ["abab", "abAabf", " aba", "ABAA", "aba"], "col2" : [1, 12, 123, 1234, 12345]})

print(df["col1"].astype(str).str.lower())
print(df["col1"].astype(str).str.upper())