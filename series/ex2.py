import pandas as pd

s = pd.Series([3, 2, 1, 5, 6])
p_list = s.tolist()
print(p_list)
print(type(p_list))