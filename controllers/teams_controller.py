from flask import Flask, render_template, request, redirect
from flask import Blueprint

teams_blueprint = Blueprint("tasks", __name__)

@teams_blueprint.route("/teams")
def teams():
    return render_template('teams.html', title="Teams")