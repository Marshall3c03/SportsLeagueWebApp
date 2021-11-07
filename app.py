from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return "Hello World"

@app.route('/table')
def tablepage():
    return "Chelsea on top"

@app.route('/about')
def aboutpage():
    return "Premier League is great"

if __name__ == '__main__':
    app.run(debug=True)
