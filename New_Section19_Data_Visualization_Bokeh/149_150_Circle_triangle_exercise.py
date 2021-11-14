# Make a basic line graph

from bokeh.plotting import figure
from bokeh.io import show, output_file
import os

x = [0, 0, 5, -5]
y = [5, -5, 0, 0]

fig = figure()
fig.triangle(x, y)
# print(__file__)
print(os.path.basename(__file__))
filename = os.path.basename(__file__)
output_file("./plots/" + filename[0:-2] + "html")
show(fig)

# will show only points plotted at the coordinates

