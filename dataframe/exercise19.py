import pandas as pd

def drop_column(df, column_name):
    df.drop(column_name, axis=1, inplace=True)

def drop_column2(df, column_name):
    df.pop(column_name)

df = pd.DataFrame({"a": [1, 2, 3], "b": [2, 3, 4], "c": [3, 4, 5]})
# drop_column(df, "b")
drop_column2(df, "b")
print(df)