class Game:

    def __init__(self, result = None, id = None):
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