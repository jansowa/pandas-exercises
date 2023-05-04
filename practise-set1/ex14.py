import pandas as pd
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print(diamonds.sort_values(by="carat", ascending=False))
print(diamonds.sort_values(by="carat", ascending=True))
