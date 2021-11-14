# Make a basic line graph

from bokeh.plotting import figure
from bokeh.io import show, output_file
import os

x = [1, 2, 3, 4, 5]
y = [11, 22, 33, 44, 55]

fig = figure()
fig.line(x, y)
# print(__file__)
print(os.path.basename(__file__))
filename = os.path.basename(__file__)
output_file("./plots/" + filename[0:-2] + "html")
show(fig)
