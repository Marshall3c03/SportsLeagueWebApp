import pdb
from re import match
from models.match import Match
from models.team import Team

import repositories.team_repository as team_repository
import repositories.match_repository as match_repository

team_1= Team('Arsenal')
team_2= Team('Aston Villa')
team_3= Team('Brentford')
team_4= Team('Brighton & Hove Albion')
team_5= Team('Burnley')
team_6= Team('Chelsea')
team_7= Team('Crystal Palace')
team_8= Team('Everton')
team_9= Team('Leeds United')
team_10= Team('Leicester City')
team_11= Team('Liverpool')
team_12= Team('Manchester City')
team_13= Team('Manchester United')
team_14= Team('Newcastle United')
team_15= Team('Norwich City')
team_16= Team('Southampton')
team_17= Team('Tottenham Hotspur')
team_18= Team('Watford')
team_19= Team('West Ham United')
team_20= Team('Wolverhampton Wanderers')

team_repository.save(team_1)
team_repository.save(team_2)
team_repository.save(team_3)
team_repository.save(team_4)
team_repository.save(team_5)
team_repository.save(team_6)
team_repository.save(team_7)
team_repository.save(team_8)
team_repository.save(team_9)
team_repository.save(team_10)
team_repository.save(team_11)
team_repository.save(team_12)
team_repository.save(team_13)
team_repository.save(team_14)
team_repository.save(team_15)
team_repository.save(team_16)
team_repository.save(team_17)
team_repository.save(team_18)
team_repository.save(team_19)
team_repository.save(team_20)