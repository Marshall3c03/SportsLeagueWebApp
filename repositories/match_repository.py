import pdb
from typing import Match
from db.run_sql import run_sql

from models.match import Match
import repositories.team_repository as team_repository

def save(match):
    sql = "INSERT INTO matches (home_team_id, away_team_id, result) VALUEs (%s,%s,%s) RETURNING *"
    values = [match.home_team.id,match.away_team.id,match.result]
    result = run_sql(sql,values)
    match_id = result[0]['id']
    match.id = match_id
    return match

def select_all():
    matches = []

    sql = "SELECT * FROM matches"
    results = run_sql(sql)

    for row in results:
        home_team = team_repository.select(row['home_team_id'])
        away_team = team_repository.select(row['away_team_id'])
        match = Match(home_team, away_team, row['result'], row['id'] )
        matches.append(match)
    return matches

def select(id):
    sql = "SELECT * FROM matches WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]

    if result is not None:
        home_team = team_repository.select(result['home_team_id'])
        away_team = team_repository.select(result['away_team_id'])
        match = Match(home_team ,away_team ,result['result'],result['id'])
    return match