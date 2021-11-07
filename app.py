from flask import Flask, render_template

from controllers.teams_controller import teams_blueprint


app = Flask(__name__)

app.register_blueprint(teams_blueprint)

@app.route('/')
def homepage():
    return render_template('table.html', title= "Table")

@app.route('/about')
def aboutpage():
    return render_template('about.html', title= "About")

if __name__ == '__main__':
    app.run(debug=True)
