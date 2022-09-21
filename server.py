from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(f'{page_name}.html')


def write_to_csv(data):
    with open('database.csv', 'a', newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thank_you')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong, try again'
