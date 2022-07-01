import pandas as pd

def find_column_max(df, column):
    return df[column].max()

df = pd.DataFrame({"a": [1, 2, 3, 1, 2, 3, 1, 2, 3], "b": [2, 3, 4, 5, 6, 7, 8, 9, 10], "c": [3, 4, 5, 6, 7, 8, 9, 10, 11]})

# print(df["b"].max())

print(find_column_max(df, "c"))