import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print(diamonds.groupby(by="cut")["price"].max().sort_values())
print(diamonds.groupby(by="cut")["price"].min().sort_values())
print(diamonds.groupby(by="cut")["cut"].count().sort_values())
