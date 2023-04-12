import pandas as pd

s = pd.Series(range(5), index=['A', 'B', 'C', 'D', 'E'])

print(pd.DataFrame(s).reset_index())