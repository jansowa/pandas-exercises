import pandas as pd

def get_column_names(df):
    return df.columns.values

df = pd.DataFrame({"a": [1, 2, 3], "b": [2, 3, 4], "c": [3, 4, 5]})

print(get_column_names(df))