import pandas as pd

df = pd.DataFrame({"col1" : ["!!ab  ", "!$12", "12!@", "   ", "!@#$"], "col2" : [1, 2, 3, 4, 5], "col3": ["ab", "ABA", "AbF", "RF_", "ab_"]})

print(df["col1"].str.isupper())
print(df["col2"].astype(str).str.isupper())
print(df["col3"].str.isupper())


print(df["col1"].str.islower())
print(df["col2"].astype(str).str.islower())
print(df["col3"].str.islower())