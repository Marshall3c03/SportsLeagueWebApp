import pdb
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
    home_team = team_repository.select(home_team_id)
    away_team_id = request.form['away_team_id']
    away_team = team_repository.select(away_team_id)
    home_score = request.form['home_score']
    away_score = request.form['away_score']
    result = request.form['result']

    newmatch = Match(home_team, away_team, home_score, away_score, result)
    match_repository.save(newmatch)
    return redirect('/matches')

@matches_blueprint.route('/match/<id>', methods=['GET'])
def show_match(id):
    match = match_repository.select(id)
    return render_template('matches/showmatch.html', match = match)

@matches_blueprint.route('/matches/<id>/edit', methods=['GET'])
def edit_match(id):
    match = match_repository.select(id)
    matches = match_repository.select_all()
    teams = team_repository.select_all()
    return render_template('/matches/editmatch.html', all_matches=matches, all_teams = teams, match=match)

@matches_blueprint.route('/match/<id>', methods=['POST'])
def update_match(id):
    pdb.set_trace()
    home_team_id = request.form['home_team_id']
    home_team = team_repository.select(home_team_id)
    away_team_id = request.form['away_team_id']
    away_team = team_repository.select(away_team_id)
    home_score = request.form['home_score']
    away_score = request.form['away_score']
    result = request.form['result']

    match = Match(home_team, away_team, home_score, away_score, result,id)
    match_repository.update(match)
    return redirect('/matches')

@matches_blueprint.route('/match/<id>/delete', methods=['POST'])
def delete_match(id):
    match_repository.delete(id)
    return redirect('/matches')