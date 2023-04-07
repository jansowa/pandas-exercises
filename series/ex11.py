import pandas as pd

s = pd.Series([100, 200, "python", 300.12, 400])

print(s.astype(dtype=str).sort_values())
