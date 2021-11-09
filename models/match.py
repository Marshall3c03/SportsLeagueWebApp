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

    def determine_club_awared_points(self,result):
        points = 0
        if result == None:
            return "Enter a valid result (Win, Draw, Loss)"
        elif result.lower() == "win":
            points += 3
        elif result.lower() == "draw":
            points += 1
        return points