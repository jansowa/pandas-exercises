import pandas as pd

df = pd.DataFrame({"col1" : ["abcab", "fge", "aabaa", "ertabes"], "col2" : [1, 2, 3, 4]})

print(df["col1"].str.count("ab"))