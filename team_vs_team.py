import pandas as pd

from pre_processing_data import concatenate_datas
from team_statistics import TeamStatistic

class TeamvsTeam(TeamStatistic):
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team
        
        self.hts = TeamStatistic(self.home_team, specific='Home', gols=2.5, year='last')
        self.ats = TeamStatistic(self.away_team, specific='Away', gols=2.5, year='last')
        
        
    def last_games(self):
        df = self.hts.data
        self.data_filter = df[((df['HomeTeam'] == self.home_team) & (df['AwayTeam'] == self.away_team)) | ((df['HomeTeam'] == self.away_team) & (df['AwayTeam'] == self.home_team))]
        try:
            print(self.data_filter)
        except:
            print('This teams dont playied yet')
        
        # self.statistic_at_game()
        
    def description(self):
        self.hts.description()
        self.ats.description()
        # self.total_mean_fouls = self.hts.mean_team_fouls + self.ats.mean_team_foulss
        # self.total_mean_yellow_card = self.hts.mean_team_yellow_cards + self.ats.mean_team_yellow_cards
        
        # print('--------------------------------------\n'
        #     f'Total fouls commited: { self.total_mean_fouls } \n'
        #     f'Total yellow card: { self.total_mean_yellow_card }\n')
      
tvt = TeamvsTeam('Chelsea', 'Burnley')
tvt.description()