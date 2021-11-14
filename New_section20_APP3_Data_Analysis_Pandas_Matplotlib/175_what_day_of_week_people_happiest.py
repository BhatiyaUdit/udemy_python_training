import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

###
# IF the Average RAting of all the courses is maximum on particular day
#   We can consider that day to be happiest #
# #

# X-axis Seven Days Y Axis Average of all courses


df = pandas.read_csv("./data/reviews.csv", parse_dates=['Timestamp'])
print(df.head())
df['Day'] = df['Timestamp'].dt.weekday
gg = df.groupby('Day').mean()
print(gg)

week = {0: "Mon", 1: "Tues", 2: "Wed", 3: "Thurs", 4: "Fri", 5: "Sat", 6: 'Sun'}
d = []
for x in gg.index:
    print(x)
    d.append(week.get(x))
print(d)
# d = gg.index.apply(lambda x : week.get(x))
# d
plt.plot(d, gg['Rating'])
plt.show()

# Instructor Method
df['WeekDay'] = df['Timestamp'].dt.strftime("%A")
df['DayNum'] = df['Timestamp'].dt.strftime("%w")
df_DD = df.groupby(['WeekDay', "DayNum"]).mean()
df_DD = df_DD.sort_values("DayNum")
print(df_DD.index.get_level_values(0))
plt.plot(df_DD.index.get_level_values(0), df_DD['Rating'])
plt.show()
