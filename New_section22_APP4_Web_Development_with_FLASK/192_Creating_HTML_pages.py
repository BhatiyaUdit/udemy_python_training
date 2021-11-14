from flask import Flask, render_template

# Renderer template method is used to return HTML pages
# Requirement : files should be present in a parallel template folder
#              but as an argument file name is enough

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)

# html,body,thead,tbody,tfoot