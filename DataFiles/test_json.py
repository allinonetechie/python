import pandas as pd

df = pd.read_json('/Users/waqasahmed/Github Repo/python/python/DataFiles/data.json')

print(df.to_string())