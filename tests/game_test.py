import unittest
from models.game import Game

class TestGame(unittest.TestCase):
    
    def setUp(self):
        self.testgame = Game()

    def test_game__has_none_result(self):
        self.testgame = Game()
        self.assertEqual(None , self.testgame.result)

    def test_game__has_win_result(self):
        self.testgame = Game("Win")
        self.assertEqual("Win", self.testgame.result)

    def test_game__has_draw_result(self):
        self.testgame = Game("Draw")
        self.assertEqual("Draw", self.testgame.result)

    def test_game__has_loss_result(self):
        self.testgame = Game("Loss")
        self.assertEqual("Loss", self.testgame.result)