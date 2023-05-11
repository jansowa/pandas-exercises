import pandas as pd
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("Number of columns:", diamonds.shape[1])
print("Number of rows:", diamonds.shape[0])

print(diamonds.dropna())
