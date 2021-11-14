from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://udit:udit1234@localhost/height_collector'
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = 'height_data'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    height = db.Column(db.Integer)

    def __init__(self, email, height):
        self.email = email
        self.height = height


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

        data_to_store = Data(email=email, height=height)

        # Scenario where email unique is violated
        # Query the data from the DB and check the entered email is present or not
        # if not present then move ahead

        print(db.session.query(Data).filter(Data.email == email))
        print(db.session.query(Data).filter(Data.email == email).count())
        if db.session.query(Data).filter(Data.email == email).count() >= 1:
            # render index.html to retry and pass message
            return render_template("success.html", text="This email is already present !! Try another one")
        else:
            print("Inside else send email")
            send_email(email, height, 165)
            db.session.add(data_to_store)
            db.session.commit()
    return render_template("success.html")


if __name__ == '__main__':
    app.debug = True
    app.run()

##
# To Browse to the success page we need to put the syntax in form action
# form action = {{url_for('success_method_name')}}
# #
##
