import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

# Data is downsampled to gain more insight

df = pandas.read_csv("./data/reviews.csv", parse_dates=['Timestamp'])
print(df.head())
df['Month'] = df['Timestamp'].dt.strftime("%Y-%m")
grouped_data = df.groupby(["Month", 'Course Name']).mean()
print(grouped_data)

# unstaacking data to create columns from extra index
grouped_data = grouped_data.unstack()
print(grouped_data)

# plotting multiple columns using pandas df.plot

print(grouped_data.plot())

# this plot will be visible as graph in jupyter

# plt.figure(figsize=(22, 3))
# plt.plot(grouped_data.index, grouped_data['Rating'])
# plt.show()
