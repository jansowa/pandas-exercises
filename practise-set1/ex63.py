import pandas as pd
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

sample = diamonds.sample(frac=0.75)

not_in_sample = diamonds[~diamonds.index.isin(sample.index)]

print(not_in_sample)
