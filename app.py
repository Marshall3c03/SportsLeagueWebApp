from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('table.html', title= "Table")

@app.route('/teams')
def teamspage():
    return render_template('teams.html', title="Teams")

@app.route('/about')
def aboutpage():
    return render_template('about.html', title= "About")

if __name__ == '__main__':
    app.run(debug=True)
