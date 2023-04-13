import pandas as pd

s = pd.Series(["abc", "Defg", "dfHEad"])

print(s.str.upper())
print(s.str.lower())
print(s.str.len())