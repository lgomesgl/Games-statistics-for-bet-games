'''
    Input -> The league
    Return -> A description with the ranking of the teams by some statistics.
'''
import pandas as pd
import numpy as np
import json

from team_statistics import TeamStatistic


class LeagueStatistics:
    def __init__(self, league_name, year):
        self.league = league_name
        self.year = year
        self.teams_analysis = []
        
    def get_the_teams(self):
        file_path = r'D:\LUCAS\Football_2.0\team_leagues.json'
        with open(file_path, "r") as file:
            data = json.load(file)
            for league in data['leagues']:
                try:
                    if league['name'] == self.league:                  
                        self.teams = [team['name'] for team in league['teams']]
                except:
                    print('This league doesnt exist')
                    
    def get_info_about_team(self):
        for team in self.teams:
            print(team)
            self.teams_analysis.append(TeamStatistic(team,specific='Home', gols=2.5, year=self.year))
            
    def create_data_league(self):
        team_statistics = []
        for team_analyse in self.teams_analysis:
            team_statistics.append({'Team':team_analyse.team, 'Mean shoots':team_analyse.mean_team_shoots, 'Mean target shoots': team_analyse.mean_team_shoots_target,
                                    'Mean corners':team_analyse.mean_team_corners, 'Mean fouls': team_analyse.mean_team_fouls, 'Mean yellow cards':team_analyse.mean_team_yellow_cards,
                                    'Percent >2.5 gols':team_analyse.percent_gols_more})
        self.data_league = pd.DataFrame.from_dict(team_statistics)
                                
ls = LeagueStatistics("Premier League", year='all')  
ls.get_the_teams()
ls.get_info_about_team()         
ls.create_data_league()      