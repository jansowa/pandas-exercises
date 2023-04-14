import pandas as pd

df = pd.DataFrame({"col1" : ["!!ab  ", "!$12", "12!@", "   ", "!@#$"], "col2" : [1, 2, 3, 4, 5]})

print(df["col1"].str.contains("[a-zA-Z]"))