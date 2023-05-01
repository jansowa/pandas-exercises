import pandas as pd
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print(diamonds.select_dtypes(object).head())
print(diamonds.describe(include=['object']))
