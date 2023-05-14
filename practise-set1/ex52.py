import pandas as pd
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print(diamonds.iloc[0:3, [diamonds.columns.get_loc('color'), diamonds.columns.get_loc('price')]])

print(diamonds.loc[0:2, ['color', 'price']])
