import pandas as pd

s = pd.Series(["Red", "Green", "Orange", "Pink", "Yellow", "White"])
print(s[s.str.count("[aeiouAEIOU]") > 1])