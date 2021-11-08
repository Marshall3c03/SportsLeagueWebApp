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