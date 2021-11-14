import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

# Data is downsampled to gain more insight

df = pandas.read_csv("./data/reviews.csv", parse_dates=['Timestamp'])
print(df.head())
df['Month'] = df['Timestamp'].dt.strftime("%Y-%m")
grouped_data = df.groupby("Month").mean()
print(grouped_data)
plt.figure(figsize=(22, 3))
plt.plot(grouped_data.index, grouped_data['Rating'])
plt.show()
