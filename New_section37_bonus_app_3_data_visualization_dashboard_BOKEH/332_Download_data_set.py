from pandas_datareader import data
from datetime import datetime

start_date = datetime(2021, 11, 1)
end_date = datetime(2021, 11, 15)

df = data.DataReader(name='HINDUNILVR.NS', data_source='yahoo', start=start_date, end=end_date)
print(df)
