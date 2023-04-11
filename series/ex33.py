import pandas as pd

text = "abc def abcdef icd"
s = pd.Series(list(text))
least_frequent = s.value_counts().index[-1]

print(text.replace(" ", least_frequent))