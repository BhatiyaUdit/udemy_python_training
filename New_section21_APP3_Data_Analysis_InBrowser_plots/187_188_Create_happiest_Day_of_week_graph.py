import pandas
import justpy

df = pandas.read_csv("./data/reviews.csv", parse_dates=['Timestamp'])
print(df.head())

# To find happiest day of the week
# Assuming the highest the rate on the day of the week
# on that day people are happy

df['WeekDay'] = df['Timestamp'].dt.strftime('%A')
df['DayNumber'] = df['Timestamp'].dt.strftime("%w")

print(df.head())

grouped_data = df.groupby(['WeekDay', 'DayNumber']).mean()
print(grouped_data.head())
grouped_data = grouped_data.sort_values(['DayNumber'])
print(grouped_data)

chart_def = """ 
  {
  chart: {
    type: 'spline'
  },
  title: {
    text: 'Average fruit consumption during one week'
  },
  legend: {
    layout: 'vertical',
    align: 'left',
    verticalAlign: 'top',
    x: 150,
    y: 100,
    floating: true,
    borderWidth: 1,
    backgroundColor: '#FFFFFF'
  },
  xAxis: {
    categories: [
      'Monday',
      'Tuesday',
      'Wednesday',
      'Thursday',
      'Friday',
      'Saturday',
      'Sunday'
    ],
    plotBands: [{ // visualize the weekend
      from: 4.5,
      to: 6.5,
      color: 'rgba(68, 170, 213, .2)'
    }]
  },
  yAxis: {
    title: {
      text: 'Fruit units'
    }
  },
  tooltip: {
    shared: true,
    valueSuffix: ' units'
  },
  credits: {
    enabled: false
  },
  plotOptions: {
    areaspline: {
      fillOpacity: 0.5
    }
  },
  series: [{
    name: 'John',
    data: [3, 4, 3, 5, 4, 10, 12]
  }, {
    name: 'Jane',
    data: [1, 3, 4, 3, 3, 5, 4]
  }]
}
"""


def app():
    quasar_page = justpy.QuasarPage()
    h1 = justpy.QDiv(a=quasar_page, text="Exercise :: Happiest Day of the Week", classes="text-h4 text-center q-pa-md")
    chart = justpy.HighCharts(a=quasar_page, options=chart_def)
    print(chart.options)
    chart.options.title.text = "Happiest Day of the week"
    print(grouped_data.index.get_level_values(0))
    chart.options.xAxis.categories = list(grouped_data.index.get_level_values(0))
    chart.options.yAxis.title.text = "Average Rating"
    chart.options.xAxis.title.text = "Day of the Week"
    chart.options.series = [{"name": "Average Rating", "data": list(grouped_data['Rating'])}]
    return quasar_page


justpy.justpy(app)
