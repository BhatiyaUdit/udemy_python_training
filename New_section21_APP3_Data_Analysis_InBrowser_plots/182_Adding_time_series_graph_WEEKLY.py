import justpy as jp
import pandas

chart_def = """ {
  chart: {
    type: 'spline',
    inverted: true
  },
  title: {
    text: 'Atmosphere Temperature by Altitude'
  },
  subtitle: {
    text: 'According to the Standard Atmosphere Model'
  },
  xAxis: {
    reversed: false,
    title: {
      enabled: true,
      text: 'Altitude'
    },
    labels: {
      format: '{value} km'
    },
    accessibility: {
      rangeDescription: 'Range: 0 to 80 km.'
    },
    maxPadding: 0.05,
    showLastLabel: true
  },
  yAxis: {
    title: {
      text: 'Temperature'
    },
    labels: {
      format: '{value}°'
    },
    accessibility: {
      rangeDescription: 'Range: -90°C to 20°C.'
    },
    lineWidth: 2
  },
  legend: {
    enabled: false
  },
  tooltip: {
    headerFormat: '<b>{series.name}</b><br/>',
    pointFormat: '{point.x} km: {point.y}°C'
  },
  plotOptions: {
    spline: {
      marker: {
        enable: false
      }
    }
  },
  series: [{
    name: 'Temperature',
    data: [
      [0, 15],
      [10, -50],
      [20, -56.5],
      [30, -46.5],
      [40, -22.1],
      [50, -2.5],
      [60, -27.7],
      [70, -55.7],
      [80, -76.5]
    ]
  }]
}"""

df = pandas.read_csv("./data/reviews.csv", parse_dates=['Timestamp'])
df['Week'] = df['Timestamp'].dt.strftime("%Y-%U")
print(df.head())
grouped_data = df.groupby("Week").mean()
print(grouped_data.head())


def app():
    qp = jp.QuasarPage()
    h1 = jp.QDiv(a=qp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=qp, text="These Graphs represent course review analysis", classes="text-h4 text-center shadow-4")
    chart = jp.HighCharts(a=qp, options=chart_def)
    print("Chart options ", chart.options)
    chart.options.chart.inverted = False
    chart.options.title.text = "Average Rating by Week"

    # Changing labels, titles etc.
    chart.options.xAxis.title.text = "Week of Year"
    chart.options.xAxis.labels.format = "{value}"

    chart.options.yAxis.title.text = "Average Rating"
    chart.options.xAxis.labels.format = "{value}"

    # Name on hover
    chart.options.series[0].name = "Average Rating"
    chart.options.tooltip.pointFormat = "{point.x} : {point.y}"

    # Point.x will be the index of the list (count of the row)
    chart.options.subtitle = ""

    print(chart.options.xAxis.labels.format)
    chart.options.xAxis.categories = list(grouped_data.index)
    chart.options.series[0].data = list(grouped_data['Rating'])

    return qp


jp.justpy(app, port=8001)
