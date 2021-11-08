import re
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.team import Team
from repositories import team_repository

teams_blueprint = Blueprint("tasks", __name__)

@teams_blueprint.route("/teams")
def teams():
    teams = team_repository.select_all()
    return render_template('teams.html', title="Teams",all_teams=teams)

@teams_blueprint.route("/newteam", methods=['GET'])
def newteam():
    return render_template('/teams/newteam.html', title="New Team",)

@teams_blueprint.route('/teams', methods=['POST'])
def createteam():
    name = request.form['teamname']
    position = request.form['position']
    gamesplayed = request.form['gamesplayed']
    wins = request.form['wins']
    draws = request.form['draws']
    loses = request.form['loses']
    points = request.form['points']

    newteam = Team(name, position,gamesplayed,wins,draws,loses,points)
    team_repository.save(newteam)
    return redirect('/teams')
