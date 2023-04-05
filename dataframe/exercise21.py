import pandas as pd

def print_rows(df):
    for index, row in df.iterrows():
        print(row)

df = pd.DataFrame({"a": [1, 2, 3], "b": [2, 3, 4], "c": [3, 4, 5]})

print(df)

# for index, row in df.iterrows():
#     print(row)
print_rows(df)