import justpy as jp
import pandas

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
        align: 'right',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: false,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
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

###############################################
#  USING AREA SPLINE CHART/ SPLINE
#############################################

df = pandas.read_csv("./data/reviews.csv", parse_dates=['Timestamp'])
df['Month'] = df['Timestamp'].dt.strftime("%Y-%m")
print(df.head())
grouped_data = df.groupby(["Month", "Course Name"])['Rating'].mean()
print(grouped_data.head())
grouped_data = grouped_data.unstack()
print(grouped_data.head())
print(grouped_data['The Python Mega Course: Build 10 Real World Applications'])


def app():
    qp = jp.QuasarPage()
    h1 = jp.QDiv(a=qp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=qp, text="These Graphs represent course review analysis", classes="text-h4 text-center shadow-4")
    chart = jp.HighCharts(a=qp, options=chart_def)
    print("Chart options ", chart.options)
    chart.options.chart.inverted = False
    chart.options.title.text = "Average Rating by Month"

    # Changing labels, titles etc.
    chart.options.xAxis.title.text = "Month of Year"
    chart.options.xAxis.labels.format = "{value}"

    chart.options.yAxis.title.text = "Average Rating"
    chart.options.xAxis.labels.format = "{value}"

    # Name on hover
    chart.options.tooltip.pointFormat = "<div style=\"color : {series.color}\">HAHAHA</div>" \
                                        " <b>{series.name}</b> : {point.y} <br/>"

    # Point.x will be the index of the list (count of the row)
    chart.options.subtitle = ""

    print(chart.options.xAxis.labels.format)
    chart.options.xAxis.categories = list(grouped_data.index)
    index = 0
    chart.options.series = []
    print("Columns", grouped_data.columns)
    for x in grouped_data.columns:
        chart.options.series.append({"name": x, "data": list(grouped_data[x])})
        # chart.options.series[index].data = list(grouped_data['Rating'][x])
        print("x = ", x)
        # index = index + 1

    # chart.options.series[0].data = list(
    #     grouped_data['Rating']['The Python Mega Course: Build 10 Real World Applications'])

    return qp


jp.justpy(app, port=8000)
