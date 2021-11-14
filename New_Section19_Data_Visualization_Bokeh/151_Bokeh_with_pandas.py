# Make a basic line graph

from bokeh.plotting import figure
from bokeh.io import show, output_file
import os
import pandas

df = pandas.read_csv("./data/data.csv")

x = df['x']
y = df['y']

print(type(x))

fig = figure()
fig.line(x, y)
# print(__file__)
print(os.path.basename(__file__))
filename = os.path.basename(__file__)
output_file("./plots/" + filename[0:-2] + "html")
show(fig)

# bokeh is able to read both python simple list as well as pandas dataFrame series

