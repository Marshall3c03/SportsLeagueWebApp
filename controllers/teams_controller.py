from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import team_repository

teams_blueprint = Blueprint("tasks", __name__)

@teams_blueprint.route("/teams")
def teams():
    teams = team_repository.select_all()
    return render_template('teams.html', title="Teams",all_teams=teams)

@teams_blueprint.route("/newteam", methods=['GET'])
def newteam():
    return render_template('newteam.html', title="New Team",)