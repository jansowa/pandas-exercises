import pandas as pd

def rename_column_name(df, old_name, new_name):
    return df.rename(columns={old_name:new_name})

df = pd.DataFrame({"a": [1, 2, 3, 1, 2, 3, 1, 2, 3], "b": [2, 3, 4, 5, 6, 7, 8, 9, 10], "c": [3, 4, 5, 6, 7, 8, 9, 10, 11]})

print(rename_column_name(df, "a", "renamed a"))