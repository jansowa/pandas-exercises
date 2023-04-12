import pandas as pd

s = pd.Series([1, 3, 7, 12, 88, 23, 0, 1, 88, 0], index=list("ABCDEFGHIJ"))

print(s.argmax())
print(s.argmin())

print(s.idxmax())
print(s.idxmin())