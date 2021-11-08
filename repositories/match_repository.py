import pdb
from typing import Match
from db.run_sql import run_sql

from models.match import Match
import repositories.team_repository as team_repository

def save(match):
    sql = "INSERT INTO matches (home_team_id, away_team_id, result) VALUEs (%s,%s,%s) RETURNING *"
    values = [match.home_team.id,match.away_team.id,match.result]
    result = run_sql(sql,values)

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
    result = run_sql(sql,values)
    pdb.set_trace()

    if result is not None and result[0] is not None:
        home_team = team_repository.select(result[0]['home_team_id'])
        away_team = team_repository.select(result[0]['away_team_id'])
        match = Match(home_team ,away_team ,result[0]['result'],result[0]['id'])
    return match