from pandas_datareader import data
from datetime import datetime

from bokeh.plotting import figure, output_file, show

start_date = datetime(2021, 11, 1)
end_date = datetime(2021, 11, 15)

df = data.DataReader(name='HINDUNILVR.NS', data_source='yahoo', start=start_date, end=end_date)
print(df)

fig = figure(x_axis_type='datetime', width=1000, height=500)
# fig.title("Candle Stick")

fig.rect(df.index, (df.Open + df.Close) / 2, 12 * 60 * 60 * 1000, abs(df.Open - df.Close))
show(fig)
