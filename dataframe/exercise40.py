import pandas as pd

def shuffle_dataframe(df):
    return df.sample(frac=1)

df = pd.DataFrame({"a": [1, 2, 3, 1, 2, 3, 1, 2, 3], "b": [2, 3, 4, 5, 6, 7, 8, 9, 10], "c": [3, 4, 5, 6, 7, 8, 9, 10, 11]})

print(shuffle_dataframe(df))