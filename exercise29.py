import pandas as pd

def remove_by_column_value(df, column_name, value):
    return df[df[column_name] != value]

df = pd.DataFrame({"a": [1, 2, 3, 1, 2, 3, 1, 2, 3], "b": [2, 3, 4, 5, 6, 7, 8, 9, 10], "c": [3, 4, 5, 6, 7, 8, 9, 10, 11]})

print(df[df.a!=1])

print(remove_by_column_value(df, "a", 1))