import pandas as pd

def convert_date(df, column):
    df[column] = pd.to_datetime(df[column])
    return df

df = pd.DataFrame({"name": ["John", "Kate", "Lucy"], "date": ["3/11/2000", "3/12/2000", "3/13/2000"]})

print(convert_date(df, "date"))