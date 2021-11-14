import os
from bokeh.plotting import figure, output_file, show

p = figure(plot_width=500, plot_height=400, tools='pan')

p.title.text = "Cool Data"
p.title.text_color = "Gray"
p.title.text_font = "times"
p.title.text_font_style = "bold"
p.xaxis.minor_tick_line_color = None
p.yaxis.minor_tick_line_color = None
p.xaxis.axis_label = "Date"
p.yaxis.axis_label = "Intensity"

p.line([1, 2, 3], [4, 5, 6])
print(os.path.basename(__file__))
filename = os.path.basename(__file__)
output_file("./plots/" + filename[0:-2] + "html")
show(p)