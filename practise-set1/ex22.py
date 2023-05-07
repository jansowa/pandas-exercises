import pandas as pd
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

for _, row in diamonds.iterrows():
    print(row['cut'])
