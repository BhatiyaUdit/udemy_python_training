from bokeh.plotting import figure
from bokeh.io import show, output_file
import os
import pandas

# plotting multiple things glyps in one figure

df = pandas.read_csv("./data/adbe.csv", parse_dates=['Date'])

print(df)
dates = df['Date']
close_value = df['Close']

fig = figure(plot_width=1000, plot_height=600, x_axis_type="datetime")
fig.line(dates, close_value, color="orange", line_width=2)
fig.line(dates, df['High'] * 1.1, color="blue", line_width=2)
filename = os.path.basename(__file__)
output_file("./plots/" + filename[0:-2] + "html")
show(fig)

# Intro to QUAD plot
# accepts for arrays top, bottom, left, right to create a rectangular figure on the graph

# https://docs.bokeh.org/en/latest/docs/gallery.html
