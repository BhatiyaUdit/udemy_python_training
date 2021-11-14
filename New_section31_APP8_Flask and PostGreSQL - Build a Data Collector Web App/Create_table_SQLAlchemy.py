from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://udit:udit1234@localhost/height_collector'
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = 'height_data'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    height = db.Column(db.Integer)
    

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/success", methods=["POST"])
def success():
    if request.method == 'POST':
        print(request.form)
        email = request.form['email_name']
        height = request.form['height_name']

        print("Email of the USER ::: ", email)
        print("Height of the USER :::: ", height)

    return render_template("success.html")


if __name__ == '__main__':
    app.debug = True
    app.run()

##
# To Browse to the success page we need to put the syntax in form action
# form action = {{url_for('success_method_name')}}
# #
##
