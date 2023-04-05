import pandas as pd

def append_row(df, dict):
    return df.append(dict, ignore_index=True)

df = pd.DataFrame({"a": [1, 2, 3, 1, 2, 3, 1, 2, 3], "b": [2, 3, 4, 5, 6, 7, 8, 9, 10], "c": [3, 4, 5, 6, 7, 8, 9, 10, 11]})

dict = {"a": 100, "b": 101, "c": 102}

print(append_row(df, dict))