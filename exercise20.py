import pandas as pd

def add_column(df, column_name, values):
    df.loc[:, column_name] = values
    return df

def add_column2(df, column_name, values):
    df[column_name] = values

df = pd.DataFrame({"a": [1, 2, 3], "b": [2, 3, 4], "c": [3, 4, 5]})
print(add_column(df, "d", [4, 5, 6]))
