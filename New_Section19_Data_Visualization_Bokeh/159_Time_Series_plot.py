# Make a basic line graph
"""
possible attributes are above, align, aspect_ratio, aspect_scale, background, background_fill_alpha,
background_fill_color, below, border_fill_alpha, border_fill_color, center, css_classes, disabled, extra_x_ranges,
extra_x_scales, extra_y_ranges, extra_y_scales, frame_height, frame_width, height, height_policy, hidpi, inner_height,
inner_width, js_event_callbacks, js_property_callbacks, left, lod_factor, lod_interval, lod_threshold, lod_timeout,
margin, match_aspect, max_height, max_width, min_border, min_border_bottom, min_border_left, min_border_right,
min_border_top, min_height, min_width, name, outer_height, outer_width, outline_line_alpha, outline_line_cap,
outline_line_color, outline_line_dash, outline_line_dash_offset, outline_line_join, outline_line_width,
output_backend, plot_height, plot_width, renderers, reset_policy, right, sizing_mode, subscribed_events,
syncable, tags, title, title_location, toolbar, toolbar_location, toolbar_sticky, visible, width, width_policy,
x_range, x_scale, y_range or y_scale


"""


from bokeh.plotting import figure
from bokeh.io import show, output_file
import os
import pandas

df = pandas.read_csv("./data/adbe.csv", parse_dates=['Date'])

print(df)
dates = df['Date']
close_value = df['Close']

fig = figure(plot_width=1000, plot_height=600, tools='pan', x_axis_type="datetime")
fig.line(dates, close_value, color="orange", line_width=2)
filename = os.path.basename(__file__)
output_file("./plots/" + filename[0:-2] + "html")
show(fig)
