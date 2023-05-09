import pandas as pd
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print(len(diamonds["cut"].unique()))
print(diamonds["cut"].nunique())
