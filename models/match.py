class Match:

    def __init__(self, home_team, away_team, home_score, away_score, result = None, id = None):
        self.home_team = home_team
        self.away_team = away_team
        self.home_score = home_score
        self.away_score = away_score
        self.result = result
        self.id = id

    def get_match_result(home_score,away_score):
        if home_score == away_score:
            return "Draw"
        elif home_score > away_score:
            return "Home Win"
        elif home_score < away_score:
            return "Away Win"
        else:
            return None

    def determine_club_awared_points(match):
        if match.home_score > match.away_score:
           match.home_team.points +=3
        elif match.home_score < match.away_score:
            match.away_team.points +=3
        else:
            match.home_team.points +=1
            match.away_team.points +=1

    def update_gamesplayed(match):
        match.home_team.gamesplayed += 1
        match.away_team.gamesplayed += 1

    def update_wins_draws_loses(match):
        if match.result == "Draw":
            match.home_team.draws +=1
            match.away_team.draws +=1
        elif match.result == "Home Win":
            match.home_team.wins += 1
            match.away_team.loses += 1
        elif match.result == "Away Win":
            match.away_team.wins += 1
            match.home_team.loses += 1

    def update_goalsscored_goalsconceded():
        pass

    def update_goaldifference():
        pass