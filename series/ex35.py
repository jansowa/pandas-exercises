import pandas as pd

print("All sundays of 2030:")
print(pd.date_range("01-01-2030", "31-12-2030", freq="W-SUN"))
