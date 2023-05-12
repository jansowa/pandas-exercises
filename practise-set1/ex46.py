import pandas as pd
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print(diamonds["cut"].sort_values())
print(diamonds["cut"].sample(frac=1).sort_index())
