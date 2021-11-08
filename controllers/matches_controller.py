import re
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.match import Match
from repositories import match_repository

matches_blueprint = Blueprint("matches", __name__)

@matches_blueprint.route("/matches")
def matches():
    matches = match_repository.select_all()
    return render_template('matches.html', title="Matches",all_matches=matches)