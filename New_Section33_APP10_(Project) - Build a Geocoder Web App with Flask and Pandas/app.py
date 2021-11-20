from flask import Flask, render_template, request, send_file
from process_csv import process_csv_start

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/result", methods=['POST'])
def process():
    global data_frame
    if request.method == 'POST':
        # print(request.form['file_'])
        # print(type(request.form['file_']))
        print(request.files['file_'])
        request.files['file_'].save("upload.csv")
        data_frame, err = process_csv_start()
        print(err)
        if err:
            return render_template("index.html", text=err)
        return render_template("index.html", text="processed", data=data_frame.T.to_dict(),
                               download="Click to Download")


@app.route("/download")
def download_csv():
    # creating file from data frame
    data_frame.to_csv('processed.csv')
    return send_file('processed.csv')


if __name__ == '__main__':
    app.run(debug=True)
