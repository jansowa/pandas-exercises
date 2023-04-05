import pandas as pd

s1 = pd.Series([2, 4, 6, 8, 10])
s2 = pd.Series([1, 3, 5, 7, 9])

print("First series element greater than second series element:")
print(s1 > s2)
print("First series element less than second series element:")
print(s1 < s2)
print("First series element equal to second series element")
print(s1 == s2)
