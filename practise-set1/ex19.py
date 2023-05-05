import pandas as pd
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print(diamonds[diamonds["cut"].isin(['Premium', 'Ideal', 'Fair'])])
