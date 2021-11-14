import pandas
import pandas as pd

data = [
    {'hello': 1, 'mad': 2, 'world': 3},
    {'mad': 2, 'world': 3},
    {'world': 1}
]

df =pd.DataFrame(data)
print(df)
print(pandas.notnull(df))
df = df.where(pandas.notnull(df), None)
print(df)