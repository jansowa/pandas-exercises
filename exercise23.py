import pandas as pd

def rename_columns(df, new_columns):
    df.columns = new_columns

df = pd.DataFrame({"a": [1, 2, 3], "b": [2, 3, 4], "c": [3, 4, 5]})

new_columns = ["d", "e", "f"]
rename_columns(df, new_columns)
print(df)