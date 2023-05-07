import pandas as pd

def describe(dtypes: list):
    diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
    print(diamonds.describe(include=dtypes))

describe(['object'])


