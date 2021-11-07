from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return "Show Table Here"

@app.route('/teams')
def teamspage():
    return render_template('teams.html')

@app.route('/about')
def aboutpage():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
