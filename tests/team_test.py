import unittest
from models.team import Team

class TestTeam(unittest.TestCase):
    
    def setUp(self):
        self.testteam = Team("Arsenal",1,10,8,1,1,25)
        
    def test_team__has_name(self):
        self.assertEqual("Arsenal", self.testteam.name)

    def test_team__has_position(self):
        self.assertEqual(1 , self.testteam.position)

    def test_team__has_gamesplayed(self):
        self.assertEqual(10, self.testteam.gamesplayed)

    def test_team__has_wins(self):
        self.assertEqual(8 , self.testteam.wins)

    def test_team__has_draws(self):
        self.assertEqual(1 , self.testteam.draws)

    def test_team__has_loses(self):
        self.assertEqual(1 , self.testteam.loses)

    def test_team__has_points(self):
        self.assertEqual(25 , self.testteam.points)