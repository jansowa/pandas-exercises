import pandas as pd

def count_by_city(df):
    return df.groupby(by='city').size().reset_index(name="Number of people")

def count_by_city2(df):
    return df.groupby(by="city").count()

df = pd.DataFrame({'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'city': ['California', 'Los Angeles', 'California', 'California', 'California', 'Los Angeles', 'Los Angeles', 'Georgia', 'Georgia', 'Los Angeles']})

print(count_by_city(df))
print(count_by_city2(df))