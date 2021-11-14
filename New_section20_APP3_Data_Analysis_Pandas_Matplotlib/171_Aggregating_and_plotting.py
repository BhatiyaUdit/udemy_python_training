import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

df = pandas.read_csv("./data/reviews.csv", parse_dates=['Timestamp'])
print(df.head())
df['Day'] = df['Timestamp'].dt.date
# df['Factor'] = df['Rating']*2
# group by mean will calculate the mean of all ppossible columns for which mean can be calculated
grouped_data = df.groupby("Day").mean()
print(grouped_data)
plt.figure(figsize=(22, 3))
plt.plot(grouped_data.index, grouped_data['Rating'])
plt.show()
