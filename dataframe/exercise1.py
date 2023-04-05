import pandas as pd

def dataframe_from_dict(dict):
    return pd.DataFrame(dict)

print(dataframe_from_dict({'X': [78, 85, 96, 80, 86], 'Y': [84, 94, 89, 83, 86], 'Z': [86, 97, 96, 72, 83]}))