from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource
import os


def plot_graph(df):
    print(df)
    figure_time = figure(x_axis_type="datetime", title="Motion Time Graph", height=400, width=1500)
    figure_time.toolbar_location = "below"
    figure_time.yaxis.minor_tick_line_color = None
    figure_time.yaxis.ticker.desired_num_ticks = 1  # to remove grid lines from y axis

    # Since we want to display time and it is in datetime format we need to convert and pass as string
    df['Start_time_string'] = df['Start'].dt.strftime("%Y-%m-%d %H:%M:%S")
    df['End_time_string'] = df['End'].dt.strftime("%Y-%m-%d %H:%M:%S")
    hover_tool = HoverTool()
    hover_tool.tooltips = [("Start", "@Start_time_string"), ("End", "@End_time_string")]
    ds = ColumnDataSource(df)
    figure_time.add_tools(hover_tool)

    figure_time.quad(top=1, bottom=0, left='Start', right='End', color="green", source=ds)
    filename = os.path.basename(__file__)
    print(__name__)
    print("file name", filename)
    output_file("./plots/" + filename[0:-2] + "html")
    show(figure_time)

#   Works fine but for tooltips code changed
#     print(df)
#     figure_time = figure(x_axis_type="datetime", title="Motion Time Graph", height=200, width=1000)
#     figure_time.yaxis.minor_tick_line_color = None
#     figure_time.yaxis.ticker.desired_num_ticks = 1  # to remove grid lines from y axis
#
#     figure_time.quad(top=1, bottom=0, left=df['Start'], right=df['End'], color="green")
#     filename = os.path.basename(__file__)
#     print(__name__)
#     print("file name", filename)
#     output_file("./plots/" + filename[0:-2] + "html")
#     show(figure_time) #
#
