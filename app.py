# Create a simple Flask application

from flask import Flask, render_template, request, redirect, url_for

# Create the Flask app

app = Flask(__name__)

@app.route('/')
def home():
    return "<h2>Hello World!</h2>"

@app.route('/welcome')
def welcome():
    return "Welcome to Flask Tutorials"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return "The person had passed and the score is: " + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person had failed and the score is: " + str(score)

@app.route('/calculate', methods = ['POST', 'GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])

        average_marks = (maths + science + history)/3
        result = ""
        if average_marks >= 50:
            result = "Success"
        else:
            result = "Fail"

        return redirect(url_for(result))
        return render_template('result.html', results = average_marks)


@app.route('/calculatemarks')
def calculatemarks():
    return render_template('calculate.html')





 





if __name__ == '__main__':
    app.run(debug=True)