import pandas as pd

df = pd.DataFrame({"col1" : [1, 2, 3, 4, 7, 11], "col2": [4, 5, 6, 9, 5, 0], "col3": [7, 5, 8, 12, 1, 11]})
print(df.iloc[:, 0])
print(df.ix[:, 0])