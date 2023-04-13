import pandas as pd

s = pd.Series(["abc", "  d e  "])

print(s.str.lstrip().tolist())
print(s.str.rstrip().tolist())
print(s.str.replace(" ", "").tolist())