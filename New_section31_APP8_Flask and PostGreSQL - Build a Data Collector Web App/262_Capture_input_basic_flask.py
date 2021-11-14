from flask import Flask, render_template, request

app = Flask(__name__)


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
