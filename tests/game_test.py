import unittest
from models.match import Match

class TestGame(unittest.TestCase):
    
    def setUp(self):
        self.testgame = Match("Chelsea","Manchester City",)

    def test_game__has_none_result(self):
        self.testgame = Match("Chelsea","Manchester City",)
        self.assertEqual(None , self.testgame.result)

    def test_game__has_win_result(self):
        self.testgame = Match("Chelsea","Manchester City","Win")
        self.assertEqual("Win", self.testgame.result)

    def test_game__has_draw_result(self):
        self.testgame = Match("Chelsea","Manchester City","Draw")
        self.assertEqual("Draw", self.testgame.result)

    def test_game__has_loss_result(self):
        self.testgame = Match("Chelsea","Manchester City","Loss")
        self.assertEqual("Loss", self.testgame.result)

    def test_game__result_adds_3(self):
        self.testgame = Match("Chelsea","Manchester City","Win")
        self.assertEqual(3, self.testgame.get_result(self.testgame.result))

    def test_game__result_adds_1(self):
        self.testgame = Match("Chelsea","Manchester City","Draw")
        self.assertEqual(1, self.testgame.get_result(self.testgame.result))

    def test_game__result_adds_0(self):
        self.testgame = Match("Chelsea","Manchester City","Loss")
        self.assertEqual(0, self.testgame.get_result(self.testgame.result))
    
    def test_game__result_returns_invalid(self):
        self.testgame = Match("Chelsea","Manchester City",)
        self.assertEqual("Enter a valid result (Win, Draw, Loss)", self.testgame.get_result(self.testgame.result))