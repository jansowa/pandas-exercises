import pandas as pd
import numpy as np

def rows_and_columns(df):
    print("Number of rows: " + str(df.shape[0]))
    print("Number of columns: " + str(df.shape[1]))

def rows_and_columns2(df):
    print("Number of rows: " + str(len(df.axes[0])))
    print("Number of columns: " + str(len(df.axes[1])))

df = pd.DataFrame({"a": [1, 2, 3], "b": [2, 3, 4]})

rows_and_columns(df)
rows_and_columns2(df)
