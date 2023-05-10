import pandas as pd
import matplotlib.pyplot as plt
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

diamonds["cut"].value_counts().plot(kind="bar")
plt.show()
