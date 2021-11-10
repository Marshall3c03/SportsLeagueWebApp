import pdb
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.match import Match
from repositories import match_repository, team_repository
from repositories import team_repository

matches_blueprint = Blueprint("matches", __name__)

@matches_blueprint.route("/matches")
def matches():
    matches = match_repository.select_all_in_match_order()
    return render_template('matches.html', title="Matches",all_matches=matches)

@matches_blueprint.route("/newmatch", methods=['GET'])
def newmatch():
    teams = team_repository.select_all_by_alphabetical()
    return render_template('/matches/newmatch.html', title="New Match", all_teams=teams)

@matches_blueprint.route('/matches', methods=['POST'])
def creatematch():
    home_team_id = request.form['home_team_id']
    home_team = team_repository.select(home_team_id)
    away_team_id = request.form['away_team_id']
    away_team = team_repository.select(away_team_id)
    home_score = request.form['home_score']
    away_score = request.form['away_score']
    result = Match.get_match_result(home_score, away_score)
    newmatch = Match(home_team, away_team, home_score, away_score, result)
    Match.update_gamesplayed(newmatch)
    Match.update_wins_draws_loses(newmatch)
    Match.determine_club_awared_points(newmatch)
    team_repository.update(home_team)
    team_repository.update(away_team)
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
    teams = team_repository.select_all_by_alphabetical()
    return render_template('/matches/editmatch.html', all_matches=matches, all_teams = teams, match=match)

@matches_blueprint.route('/match/<id>', methods=['POST'])
def update_match(id):
    # selected match
    selected_match = match_repository.select(id)
    home_team = selected_match.home_team
    away_team = selected_match.away_team
    Match.remove_gameplayed(home_team, away_team)
    Match.remove_wins_draws_loses(selected_match, home_team, away_team)
    Match.remove_points(selected_match, home_team, away_team)
    team_repository.update(home_team)
    team_repository.update(away_team)


    # adding new info
    home_team_id = request.form['home_team_id']
    home_team = team_repository.select(home_team_id)
    away_team_id = request.form['away_team_id']
    away_team = team_repository.select(away_team_id)
    home_score = request.form['home_score']
    away_score = request.form['away_score']
    result = Match.get_match_result(home_score, away_score)
    match = Match(home_team, away_team, home_score, away_score, result,id)
       
    Match.update_gamesplayed(match)
    Match.update_wins_draws_loses(match)
    Match.determine_club_awared_points(match)
    team_repository.update(home_team)
    team_repository.update(away_team)
    match_repository.update(match)
    return redirect('/matches')

@matches_blueprint.route('/match/<id>/delete', methods=['POST'])
def delete_match(id):
    match = match_repository.select(id)
    home_team = match.home_team
    away_team = match.away_team
    Match.remove_gameplayed(home_team, away_team)
    Match.remove_wins_draws_loses(match, home_team, away_team)
    Match.remove_points(match, home_team, away_team)
    team_repository.update(home_team)
    team_repository.update(away_team)
    match_repository.delete(id)
    return redirect('/matches')