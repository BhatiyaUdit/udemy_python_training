from pandas_datareader import data
from datetime import datetime

from bokeh.plotting import figure, output_file, show

start_date = datetime(2020, 10, 1)
end_date = datetime(2021, 11, 15)
increase = 'Increase'
decrease = 'Decrease'
hours_in_milis = 12 * 60 * 60 * 1000

df = data.DataReader(name='HINDUNILVR.NS', data_source='yahoo', start=start_date, end=end_date)
print(df)

# Added these columns to easily filter data (Needed for Color changing rectangles)
df['Status'] = [increase if open_ < close_ else decrease for open_, close_ in zip(df.Open, df.Close)]
df['Middle'] = (df.Open + df.Close) / 2
df['Height'] = abs(df.Open - df.Close)

fig = figure(x_axis_type='datetime', width=1000, height=500)
fig.grid.grid_line_alpha = 0.3
# fig.title("Candle Stick")

print(df.index[df.Status == increase])

x_high = df.index
y_high = df.High
x_low = df.index
y_low = df.Low

fig.segment(x_high, y_high, x_low, y_low)

fig.rect(df.index[df.Status == increase], df.Middle[df.Status == increase], hours_in_milis,
         df.Height[df.Status == increase], fill_color='green', line_color='green')
fig.rect(df.index[df.Status == decrease], df.Middle[df.Status == decrease], hours_in_milis,
         df.Height[df.Status == decrease], fill_color='red', line_color='red')

output_file("iteration3.html")
show(fig)

