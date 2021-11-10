from flask import Flask, render_template

from controllers.teams_controller import teams_blueprint
from controllers.matches_controller import matches_blueprint
from repositories import team_repository


app = Flask(__name__)

app.register_blueprint(teams_blueprint)
app.register_blueprint(matches_blueprint)

@app.route('/')
def homepage():
    teams = team_repository.select_all_by_points()
    return render_template('table.html', title= "Table",all_teams=teams)

@app.route('/about')
def aboutpage():
    return render_template('about.html', title= "About")

if __name__ == '__main__':
    app.run(debug=True)
