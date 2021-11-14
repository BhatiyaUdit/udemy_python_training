import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

df = pandas.read_csv("./data/reviews.csv", parse_dates=['Timestamp'])
print(df.head())
df['Week'] = df['Timestamp'].dt.strftime("%Y-%U")
grouped_data = df.groupby("Week").mean()
print(grouped_data)
plt.figure(figsize=(22, 3))
plt.plot(grouped_data.index, grouped_data['Rating'])
plt.show()
