class Match:

    def __init__(self, team_1, team_2, result = None, id = None):
        self.team_1 = team_1
        self.team_2 = team_2
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