import pandas, os
from bokeh.plotting import figure
from bokeh.io import output_file, show

df = pandas.read_excel("./data/weather.xlsx", "Ark1")
print(df)

temperatures = df['Temperature']
pressures = df['Pressure']

temperatures = temperatures.apply(lambda x: x / 10)
pressures = pressures.apply(lambda x: x / 10)

figure_weather = figure(plot_width=1000, plot_height=800, tools='pan')
figure_weather.title.text = "Temperature and Air Pressure"
figure_weather.title.text_color = "Blue"
figure_weather.title.text_font = 'times'
figure_weather.title.text_font_style = "bold"

figure_weather.xaxis.axis_label = "Temperature (°C)"
figure_weather.yaxis.axis_label = "Pressure (hPa)"

figure_weather.circle(temperatures, pressures, size=2)
print(os.path.basename(__file__))
filename = os.path.basename(__file__)
output_file("./plots/" + filename[0:-2] + "html")
show(figure_weather)
