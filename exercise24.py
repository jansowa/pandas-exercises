import pandas as pd

def rows_with_value_in_column(df, column, value):
    return df[df[column] == value]

df = pd.DataFrame({"a": [1, 2, 3, 1, 2, 3, 1, 2, 3], "b": [2, 3, 4, 5, 6, 7, 8, 9, 10], "c": [3, 4, 5, 6, 7, 8, 9, 10, 11]})

print(rows_with_value_in_column(df, "a", 2))