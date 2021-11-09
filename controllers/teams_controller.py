import re
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from controllers.matches_controller import matches
from models.team import Team
from repositories import team_repository, match_repository

teams_blueprint = Blueprint("teams", __name__)

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

@teams_blueprint.route('/team/<id>', methods=['GET'])
def show_team(id):
    team = team_repository.select(id)
    matches = match_repository.select_all()
    return render_template('teams/showteam.html', team = team, all_matches=matches)

@teams_blueprint.route('/teams/<id>/edit', methods=['GET'])
def edit_team(id):
    team = team_repository.select(id)
    return render_template('/teams/editteam.html', team=team)

@teams_blueprint.route('/teams/<id>', methods=['POST'])
def update_team(id):
    name = request.form['teamname']
    position = request.form['position']
    gamesplayed = request.form['gamesplayed']
    wins = request.form['wins']
    draws = request.form['draws']
    loses = request.form['loses']
    points = request.form['points']

    team = Team(name, position,gamesplayed,wins,draws,loses,points,id)
    team_repository.update(team)
    return redirect('/teams')

@teams_blueprint.route('/teams/<id>/delete', methods=['POST'])
def delete_team(id):
    team_repository.delete(id)
    return redirect('/teams')