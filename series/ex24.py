import pandas as pd

s = pd.Series(["php", "python", "java", "c#"])

print(s.apply(lambda txt: txt[0].upper() + txt[1:]).apply(lambda txt: txt[:-1] + txt[-1].upper()))
print(s.apply(lambda txt: txt[0].upper() + txt[1:-1] + txt[-1].upper()))