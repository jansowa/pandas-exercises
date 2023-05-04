import pandas as pd
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

diamonds.columns = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(diamonds.head())