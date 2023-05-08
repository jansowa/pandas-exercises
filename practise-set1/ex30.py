import pandas as pd
import matplotlib.pyplot as plt
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

diamonds.groupby('cut')[["carat", "depth", "table", "price", "x", "y", "z"]].mean().plot(kind='bar', logy=True)
plt.show()
