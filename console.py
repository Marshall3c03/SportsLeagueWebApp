import pdb
from models.match import Match
from models.team import Team

import repositories.team_repository as team_repository
import repositories.match_repository as match_repository

match1 = Match('Chelsea','Manchester City',"Win")
match_repository.save(match1)

pdb.set_trace()