import pandas as pd
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print((diamonds["cut"].value_counts() * 100 / len(diamonds["cut"])).astype(str) + " %")
print((diamonds["cut"].value_counts(normalize=True) * 100).astype(str) + " %")
