import pandas
import justpy as jp

# To Show number of rating left per course

df = pandas.read_csv("./data/reviews.csv", parse_dates=['Timestamp'])
count_by_course = df.groupby(['Course Name'])['Rating'].count()
print(count_by_course)

chart_template = """
 {
  chart: {
    type: 'pie'
  },
  title: {
    text: 'Browser market shares in January, 2018'
  },
  tooltip: {
    pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
  },
  accessibility: {
    point: {
      valueSuffix: '%'
    }
  },
  plotOptions: {
    pie: {
      allowPointSelect: true,
      cursor: 'pointer',
      dataLabels: {
        enabled: true,
        format: '<b>{point.name}</b>: {point.percentage:.1f} %'
      }
    }
  },
  series: [{
    name: 'Brands',
    colorByPoint: true,
    data: [{
      name: 'Chrome',
      y: 61.41,
      sliced: true,
      selected: true
    }, {
      name: 'Internet Explorer',
      y: 11.84
    }, {
      name: 'Firefox',
      y: 10.85
    }, {
      name: 'Edge',
      y: 4.67
    }, {
      name: 'Safari',
      y: 4.18
    }, {
      name: 'Sogou Explorer',
      y: 1.64
    }, {
      name: 'Opera',
      y: 1.6
    }, {
      name: 'QQ',
      y: 1.2
    }, {
      name: 'Other',
      y: 2.61
    }]
  }]
}
"""


def app():
    quasar_page = jp.QuasarPage()
    h1 = jp.QDiv(a=quasar_page, text="Pie chart for Review Count", classes="text-h4 text-center q-pa-md")
    chart = jp.HighCharts(a=quasar_page, options=chart_template)
    print(chart.options)
    chart.options.title.text = "Number of Ratings per Course"
    chart.options.series[0].name = "Number of Reviews"
    for x in count_by_course.index:
        print("x", x)
        print("value", count_by_course[x])

    dl = [{"name": x, "y": count_by_course[x]} for x in count_by_course.index]
    print("DATA ::: ", dl)
    print(chart.options.series[0].data)
    chart.options.series[0].data = [{"name": x, "y": float(count_by_course[x])} for x in count_by_course.index]
    print(chart.options.series[0].data)
    return quasar_page


jp.justpy(app)

###############################################
# y attribute needs to be converted to float
###############################################