import pandas as pd

df = pd.DataFrame({"col1" : ["!!ab  ", "    a   ", "     ", "   ", "!@#$"], "col2" : [1, 12, 123, 1234, 12345]})

print(df["col2"].astype(str).str.len())