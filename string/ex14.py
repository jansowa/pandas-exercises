import pandas as pd

df = pd.DataFrame({"col1" : ["!!ab  ", "    a   ", "     ", "   ", "!@#$"], "col2" : [1, 2, 3, 4, 5], "col3": ["My NoT SO Super Title", "My Extra Title", "my bad title", "MY WEIRD TITLE", "ab_"]})

print(df["col1"].str.isspace())
print(df["col2"].astype(str).str.isspace())
print(df["col3"].str.isspace())