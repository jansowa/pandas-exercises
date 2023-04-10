import pandas as pd
from pandas.tseries.offsets import DateOffset
from dateutil.parser import parse

s = pd.Series(["Jan 2015", "Feb 2016", "Mar 2017", "Apr 2018", "May 2019"])
print(pd.to_datetime(s).dt.to_period('M').dt.to_timestamp() + DateOffset(days=10))
print(pd.to_datetime(s).apply(lambda dt: dt.replace(day=11)))
print(s.map(lambda date: parse("11 " + date)))
