import pandas as pd
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

rows, columns = diamonds.shape

print("Rows:", rows)
print("Columns:", columns)

for column in diamonds.columns:
    print(column + " column type: " + str(diamonds[column].dtypes))