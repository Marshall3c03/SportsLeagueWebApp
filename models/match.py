class Match:

    def __init__(self, home_team, away_team, result = None, id = None):
        self.home_team = home_team
        self.away_team = away_team
        self.result = result
        self.id = id

    def get_result(self,result):
        points = 0
        if result == None:
            return "Enter a valid result (Win, Draw, Loss)"
        elif result.lower() == "win":
            points += 3
        elif result.lower() == "draw":
            points += 1
        return points