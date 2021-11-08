import re
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.match import Match
from repositories import match_repository
from repositories import team_repository

matches_blueprint = Blueprint("matches", __name__)

@matches_blueprint.route("/matches")
def matches():
    matches = match_repository.select_all()
    return render_template('matches.html', title="Matches",all_matches=matches)

@matches_blueprint.route("/newmatch", methods=['GET'])
def newmatch():
    teams = team_repository.select_all()
    return render_template('/matches/newmatch.html', title="New Match", all_teams=teams)

@matches_blueprint.route('/matches', methods=['POST'])
def creatematch():
    home_team_id = request.form['home_team_id']
    home_team = match_repository.select(home_team_id)
    away_team_id = request.form['away_team_id']
    away_team = match_repository.select(away_team_id)
    result = request.form['result']

    newmatch = Match(home_team, away_team, result)
    match_repository.save(newmatch)
    return redirect('/matches')

@matches_blueprint.route('/match/<id>')
def show_match