from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("home1.html")


@app.route("/about")
def about_page():
    return render_template("about1.html")


if __name__ == '__main__':
    app.run()
