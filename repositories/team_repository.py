from re import S
from db.run_sql import run_sql

from models.team import Team

def select_all():
    teams = []

    sql = "SELECT * FROM teams"
    results = run_sql(sql)

    for row in results:
        team = Team(row['name'],row['position'],row['gamesplayed'],row['wins'],row['draws'],row['loses'],row['points'],row['id'])
        teams.append(team)
    return teams

def select(id):
    team = None
    sql = "SELECT * FROM teams WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]

    if result is not None:
        team = Team(result['name'],result['position'],result['gamesplayed'],result['wins'],result['draws'],result['loses'],result['points'],result['id'])
    return team

def save(team):
    sql = "INSERT INTO teams (name,position,gamesplayed,wins,draws,loses,points) VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING *"
    values = [team.name,team.position,team.gamesplayed,team.wins,team.draws,team.loses,team.points]
    results = run_sql(sql,values)
    id = results[0]['id']
    team.id = id
    return team

def update(team):
    sql = "UPDATE teams SET (name,position,gamesplayed,wins,draws,loses,points) = (%s,%s,%s,%s,%s,%s,%s) WHERE id = %s"
    values = [team.name,team.position,team.gamesplayed,team.wins,team.draws,team.loses,team.points, team.id]
    run_sql(sql,values)

def delete(id):
    sql = "DELETE FROM teams WHERE id = %s"
    values = [id]
    run_sql(sql,values)