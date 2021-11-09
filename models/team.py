from repositories import match_repository

class Team:

    def __init__(self, name, position = 1,gamesplayed = 0 ,wins = 0,draws = 0,loses = 0,points = 0,id = None):
        self.name = name
        self.position = position
        self.gamesplayed = gamesplayed
        self.wins = wins
        self.draws = draws
        self.loses = loses
        self.points = points
        self.id = id

    def get_matches_played(team):
        team_games = []

        matches = match_repository.select_all()
        

        for match in matches:
            if match.home_team.name == team.name:
                team_games.append(match)
            elif match.away_team.name == team.name:
                team_games.append(match)
        gamesplayed = len(team_games)

        return gamesplayed