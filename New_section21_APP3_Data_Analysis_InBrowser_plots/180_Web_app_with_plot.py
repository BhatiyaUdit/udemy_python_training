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
df['Date'] = df['Timestamp'].dt.date
print(df.head())
grouped_data = df.groupby("Date").mean()
print(grouped_data.head())


def app():
    qp = jp.QuasarPage()
    h1 = jp.QDiv(a=qp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=qp, text="These Graphs represent course review analysis", classes="text-h4 text-center shadow-4")
    chart = jp.HighCharts(a=qp, options=chart_def)
    print("Chart", chart)
    print("Chart options ", chart.options)
    chart.options.chart.inverted = False
    chart.options.title.text = "Average Rating by Day"
    # STEP 1 :::: chart.options.series[0].data = [[1, 2], [3, 4]]
    #
    # STEP 2 ::::
    # x = [1, 2, 3]
    # y = [4, 56, 6]
    # d = list(zip(x, y))
    # chart.options.series[0].data = d
    #
    # Step 3 ::::
    # x = grouped_data.index
    # y = grouped_data['Rating']
    # d = list(zip(x, y))
    # chart.options.series[0].data = d
    #
    # Step 4 :::
    # rate_strs = [str(x) for x in grouped_data['Rating']]
    # y = grouped_data['Rating']
    # s = str(grouped_data['Rating'])
    # d = list(zip(rate_strs, y))
    # print(d)
    # chart.options.series[0].data = d
    chart.options.xAxis.categories = list(grouped_data.index)
    chart.options.series[0].data = list(grouped_data['Rating'])

    return qp


jp.justpy(app)

##
#  Once the base chart is ready we can do modifications by accessing the chart definition dictionary
#  we can access the details inside def by refrencing chart.options #
#  to change any value need to refer to the options dict and we can manipulate the data
#  Example :: Title :: chart.options.title.text = "Some value"
#  Example :: PLOT Values :: chart.options.series[0].data = [[1,2], [3,4]]
#  We can adjust all the things that are needed to be changed based on this dict object ......
#
#  Converting Data from multiple lists to list of lists (as per needed by options)
#       x = [1,2,3]
#       y = [4,5,6]
#       d = list(zip(x,y))
#
#       zip will convert multiple lists to a single one but needs to cast as a list
#
#  Change inverted graph to normal one
#  chart.options.chart.inverted = False
#
#  Using data frames to create lists of the data that we need to pass
#  Import all the code from previous section for the "Day Average"
#  and write this code :
#       x = grouped_data.index
#       y = grouped_data['Rating']
#       d = list(zip(x, y))
#       chart.options.series[0].data = d
#  This will create an empty chart because date/string/etc are different objects and needs to be treated that way
#  NOTE : even String are also not acceptable
#  USE:::::::::::::::
#       chart.options.xAxis.categories = grouped_data.index {Pass complete series as the categories}
#       NOTE :: Convert Series objects to list objects   *******************
#
#       NEXT STEPS : Change labels, titles, etc
#       #
# ##
