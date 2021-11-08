from typing import Match
from db.run_sql import run_sql

from models.match import Match

def select_all():
    matches = []

    sql = "SELECT * FROM matches"
    results = run_sql(sql)

    for row in results:
        match = Match(row['team_1'],row['team_2'],row['result'],row['id'])
        matches.append(match)
    return matches

def save(match):
    sql = "INSERT INTO matches (team_1,team_2,result) VALUES (%s,%s,%s) RETURNING *"
    values = [match.team_1,match.team_2,match.result]
    results = run_sql(sql,values)
    id = results[0]['id']
    match.id = id
    return match