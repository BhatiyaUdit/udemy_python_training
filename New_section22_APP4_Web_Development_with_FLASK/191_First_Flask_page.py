from flask import Flask

app = Flask(__name__)
print(app)


@app.route("/")
def home():
    return "Home Page"


@app.route("/about")
def about():
    return "About page"


if __name__ == '__main__':
    app.run(debug=True)
