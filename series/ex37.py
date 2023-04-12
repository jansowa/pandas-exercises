import pandas as pd

s1 = pd.Series(range(5))
s2 = pd.Series(list('ABCDE'))

print("Stack vertically")
print(pd.concat([s1, s2], axis=0))

print("Stack horizontally")
print(pd.concat([s1, s2], axis=1))
