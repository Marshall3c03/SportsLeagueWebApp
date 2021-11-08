import pdb
from re import match
from models.match import Match
from models.team import Team

import repositories.team_repository as team_repository
import repositories.match_repository as match_repository

team_1 = Team('Burnley',1,11,8,2,1,26)
team_2 = Team('Watford',2,11,7,2,2,23)
team_repository.save(team_1)
team_repository.save(team_2)

match1 = Match(team_1,team_2,'Win')
match_repository.save(match1)

selectedmatch = match_repository.select(1)
hometeam = team_repository.select(selectedmatch.home)

