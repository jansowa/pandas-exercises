import pandas as pd

s = pd.Series(["01 Jan 2015", "10-02-2016", "20180307", "2014/05/06", "2016-04-12", "2019-04-06T11:20"])
s_dates = pd.to_datetime(s, format='mixed')
# print(pd.DatetimeIndex(s_dates).year)
print("Day of month:")
print(s_dates.dt.day.tolist())
print("Day of year")
print(s_dates.dt.dayofyear.tolist())
print("Week number:")
print(((s_dates.dt.dayofyear // 7) + 1).tolist())
print("Day of week:")
print(s_dates.dt.day_name().tolist())