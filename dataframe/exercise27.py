import pandas as pd

def csv_with_tab_separator(df, filename):
    df.to_csv(filename, sep="\t")

df = pd.DataFrame({"a": [1, 2, 3, 1, 2, 3, 1, 2, 3], "b": [2, 3, 4, 5, 6, 7, 8, 9, 10], "c": [3, 4, 5, 6, 7, 8, 9, 10, 11]})

# df.to_csv("file.txt", sep="\t")
csv_with_tab_separator(df, "file.txt")