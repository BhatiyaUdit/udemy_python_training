from flask import Flask, render_template
from bokeh_plot import get_plot

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/plot")
def plot():
    link, js, html = get_plot()
    return render_template("plot.html", link=link, js=js, html=html)


if __name__ == '__main__':
    app.run(debug=True, port=5005)
