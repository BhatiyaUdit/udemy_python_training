import justpy as jp
import pandas

chart_def = """ 
 {

  chart: {
    type: 'streamgraph',
    marginBottom: 30,
    zoomType: 'x'
  },

  title: {
    floating: true,
    align: 'left',
    text: 'Winter Olympic Medal Wins'
  },
  subtitle: {
    floating: true,
    align: 'left',
    y: 30,
    text: 'Source: <a href="https://www.sports-reference.com/olympics/winter/1924/">sports-reference.com</a>'
  },

  xAxis: {
    maxPadding: 0,
    type: 'category',
    crosshair: true,
    categories: [],
    labels: {
      align: 'left',
      reserveSpace: false,
      rotation: 270
    },
    lineWidth: 0,
    margin: 20,
    tickWidth: 0
  },

  yAxis: {
    visible: false,
    startOnTick: false,
    endOnTick: false
  },

  legend: {
    enabled: false
  },

  annotations: [{
    labels: [{
      point: {
        x: 5.5,
        xAxis: 0,
        y: 30,
        yAxis: 0
      },
      text: 'Cancelled<br>during<br>World War II'
    }, {
      point: {
        x: 18,
        xAxis: 0,
        y: 90,
        yAxis: 0
      },
      text: 'Python become popular'
    }],
    labelOptions: {
      backgroundColor: 'rgba(255,255,255,0.5)',
      borderColor: 'silver'
    }
  }],

  plotOptions: {
    series: {
      label: {
        minFontSize: 5,
        maxFontSize: 15,
        style: {
          color: 'rgba(255,255,255,0.75)'
        }
      }
    }
  },

  // Data parsed with olympic-medals.node.js
  series: [],

  exporting: {
    sourceWidth: 800,
    sourceHeight: 600
  }

}
"""

###############################################
#  USING STREAM CHART
#
#  Create a Stream graph of the count of ratings #
#############################################

df = pandas.read_csv("./data/reviews.csv", parse_dates=['Timestamp'])
df['Month'] = df['Timestamp'].dt.strftime("%Y-%m")
print(df.head())
grouped_data = df.groupby(["Month", "Course Name"])['Rating'].count()
print(grouped_data.head())
grouped_data = grouped_data.unstack()
print(grouped_data.head())
print(grouped_data['The Python Mega Course: Build 10 Real World Applications'])
grouped_data = grouped_data.drop("The Python Mega Course: Build 10 Real World Applications", 1)


def app():
    qp = jp.QuasarPage()
    h1 = jp.QDiv(a=qp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=qp, text="These Graphs represent course review analysis", classes="text-h4 text-center shadow-4")
    chart = jp.HighCharts(a=qp, options=chart_def)
    print("Chart options ", chart.options)
    chart.options.chart.inverted = False
    chart.options.title.text = "Rating Count by Month By Course"

    # Changing labels, titles etc.
    chart.options.xAxis.title.text = "Month of Year"
    chart.options.xAxis.labels.format = "{value}"

    chart.options.yAxis.title.text = "Rating Count"
    chart.options.xAxis.labels.format = "{value}"

    chart.options.subtitle = ""

    print(chart.options.xAxis.labels.format)
    chart.options.xAxis.categories = list(grouped_data.index)
    print("Columns", grouped_data.columns)
    chart_data = [{"name": x, "data": list(grouped_data[x])} for x in grouped_data.columns]
    chart.options.series = chart_data

    return qp


jp.justpy(app, port=8000)

# Additionsal Cleanup code
#
#     # Name on hover
#     # chart.options.tooltip.pointFormat = "<div style=\"color : {series.color}\">HAHAHA</div>" \
#     #                                     " <b>{series.name}</b> : {point.y} <br/>"
#
#     # Point.x will be the index of the list (count of the row)
#   # for x in grouped_data.columns:
#     #     chart.options.series.append({"name": x, "data": list(grouped_data[x])})
#     #     # chart.options.series[index].data = list(grouped_data['Rating'][x])
#     #     print("x = ", x)
#     #     # index = index + 1
#
#     # chart.options.series[0].data = list(
#     #     grouped_data['Rating']['The Python Mega Course: Build 10 Real World Applications'])  #
