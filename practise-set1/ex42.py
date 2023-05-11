import pandas as pd
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print(diamonds.dropna(subset=["cut", "color"]))
print(diamonds.dropna(subset=["cut", "color"], how="all"))
