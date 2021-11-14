import pandas
from datetime import datetime
from pytz import utc
# data = pandas.read_csv("./data/reviews.csv")

# print(data)

# filter data to print details of reviews in Second half of year 2020

# print(data[data['Rating'] > 4])

# Do not work ::: filter_df = data[data['Timestamp']> '1-07-2020']

# Do not work :::filter_df = data[data['Timestamp'] > datetime(2020, 6, 30)]
# TypeError: '>' not supported between instances of 'str' and 'datetime.datetime'

# Do not Work :::: Datetime obj does not have timezone
# data = pandas.read_csv("./data/reviews.csv", parse_dates=['Timestamp'])
# filter_df = data[data['Timestamp'] > datetime(2020, 6, 30)]
# TypeError: Invalid comparison between dtype=datetime64[ns, UTC] and datetime


data = pandas.read_csv("./data/reviews.csv", parse_dates=['Timestamp'])
filter_df = data[(data['Timestamp'] > datetime(2020, 6, 30, tzinfo=utc)) &
                 (data['Timestamp'] < datetime(2021, 1, 1, tzinfo=utc))]
print(filter_df)
