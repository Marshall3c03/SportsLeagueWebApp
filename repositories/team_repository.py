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

def save(team):
    sql = "INSERT INTO teams (name,position,gamesplayed,wins,draws,loses,points) VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING *"
    values = [team.name,team.position,team.gamesplayed,team.wins,team.draws,team.loses,team.points]
    results = run_sql(sql,values)
    id = results[0]['id']
    team.id = id
    return team