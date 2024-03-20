import pandas as pd

from pre_processing_data import concatenate_datas

from team_statistics import TeamStatistic


class TeamvsTeam:
    def __init__(self, home_team, away_team, specific='Home', gols=2.5, year='last'):
        self.home_team = home_team
        self.away_team = away_team

        self.hts = TeamStatistic(self.home_team, specific='Home', gols=gols, year=year)
        self.ats = TeamStatistic(self.away_team, specific='Away', gols=gols, year=year)
        
tvt = TeamvsTeam('Real Madrid', 'Getafe')
tvt.hts.description()
tvt.ats.description()