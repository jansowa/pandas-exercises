import pandas as pd
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

diamonds.drop(diamonds.columns[1], axis=1, inplace=True)
print(diamonds.head())