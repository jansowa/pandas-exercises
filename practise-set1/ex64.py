import pandas as pd
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

print("Duplicated colors:")
print(diamonds[diamonds.duplicated(subset="color")]["color"].unique())
