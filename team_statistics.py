import pandas as pd
import json
import os

from pre_processing_data import concatenate_datas

class TeamStatistic:
    def __init__(self, team, specific='Home', gols=2.5, year='last'):
        self.team = team
        self.league = None
        self.specific = specific
        # self.modeTeam = 'Home and Away'
        
        self.get_league_and_dataset(year)
        self.data = concatenate_datas(self.datasets)
        self.allocate_mode()
        self.filter_by_team()
        self.more_or_less_gols(gols)
        self.win_draw_loser_data()
        self.mean_odds()
        self.statistic_at_game()

    # def __str__(self):
    #     return f'{ self.team } at { self.modeTeam } games'
    
    def get_league_and_dataset(self, year):
        file_path = r'D:\LUCAS\Football_2.0\team_leagues.json'
        with open(file_path, "r") as file:
            data = json.load(file)
            for league in data['leagues']:
                for team in league['teams']:
                    if team['name'] == self.team:
                        self.league = league['name']
                        if year == 'last' and len(league['datasets']) > 1:
                            self.datasets = [league['datasets'][-1]]
                        else:
                            self.datasets = league['datasets']                     
                      
    def allocate_mode(self):
        if self.specific == 'Home':
            self.modeGame = 'HomeTeam'
            self.modeLett = 'H'
            self.modeLettA = 'A'
        if self.specific == 'Away':
            self.modeGame = 'AwayTeam'
            self.modeLett = 'A'
            self.modeLettA = 'H'
    
    def change_mode(self):
        if self.specific == 'Home':
            self.specific = 'Away'
        else:
            self.specific = 'Home'
       
    def filter_by_team(self):
        try:
            self.data_filter = self.data[(self.data[self.modeGame] == self.team)]
        except:
            self.data_filter = self.data[(self.data['HomeTeam'] == self.team) | (self.data['AwayTeam'] == self.team)]                                                                                                                                                                                                                                                                                        
    
    def more_or_less_gols(self, gols):
        self.gols_team_more = self.data_filter[(self.data_filter[f'FT{ self.modeLett }G'] >= gols)]        
        self.gols_team_less = self.data_filter[(self.data_filter[f'FT{ self.modeLett }G'] < gols)]
        
        self.total_more = self.data_filter[(self.data_filter['Total_gols'] >= gols)]
        self.total_less = self.data_filter[(self.data_filter['Total_gols'] < gols)]
        
    def win_draw_loser_data(self):
        self.win_data = self.data_filter[(self.data_filter['Result'] == self.modeLett)]
        self.lose_data = self.data_filter[(self.data_filter['Result'] == self.modeLettA)]
        self.draw_data = self.data_filter[(self.data_filter['Result'] == 'D')]
        
    def mean_odds(self):
        self.mean_odd_to_win = round(self.win_data[f'B365{ self.modeLett }'].describe().mean(), 2)
        self.mean_odd_to_lose = round(self.lose_data[f'B365{ self.modeLettA }'].describe().mean(), 2)
        self.mean_odd_to_draw = round(self.draw_data[f'B365D'].describe().mean(), 2)
        
        
        self.odd_total_gols_more_2_5 = round(self.total_more['B365>2.5'].describe().mean(), 2)
        self.odd_total_gols_less_2_5 = round(self.total_less['B365<2.5'].describe().mean(), 2)
        
    def statistic_at_game(self):
        self.mean_team_shoots = round(self.data_filter[f'{ self.modeLett }S'].mean(), 2)
        self.mean_team_against_shoot = round(self.data_filter[f'{ self.modeLettA }S'].mean(), 2)
        
        self.mean_team_shoots_target = round(self.data_filter[f'{ self.modeLett }ST'].mean(), 2)
        self.mean_team_against_shoots_target = round(self.data_filter[f'{ self.modeLettA }ST'].mean(), 2)
        
        self.mean_team_corners = round(self.data_filter[f'{ self.modeLett }C'].mean(), 2)
        self.mean_team_against_corners = round(self.data_filter[f'{ self.modeLettA }C'].mean(), 2)
        
        self.mean_team_fouls = round(self.data_filter[f'{ self.modeLett }F'].mean(), 2)
        self.mean_team_against_fouls = round(self.data_filter[f'{ self.modeLettA }F'].mean(), 2)
        
        self.mean_team_yellow_cards = round(self.data_filter[f'{ self.modeLett }Y'].mean(), 2)
        self.mean_team_against_yellow_cards = round(self.data_filter[f'{ self.modeLettA }Y'].mean(), 2)
        
        self.diff_gols_win = round(self.win_data['Diff_gols'].mean(), 2)
    
    def description(self):
        print(f'-----------------------DESCRIPTION-----------------------\n'
            f'{self.team} at {self.specific} games\n'
            f'Mean odds: Win-> {self.mean_odd_to_win}, Draw-> {self.mean_odd_to_draw}, Lose-> {self.mean_odd_to_lose}\n'
            f'Mean odds: {self.odd_total_gols_less_2_5} < 2.5 total gols > {self.odd_total_gols_more_2_5}\n'
            f'Mean shots by {self.team}: {self.mean_team_shoots}, by away team: {self.mean_team_against_shoot}\n'
            f'Mean target shots by {self.team}: {self.mean_team_shoots_target}, by away team: {self.mean_team_against_shoots_target}\n'
            f'Mean corners by {self.team}: {self.mean_team_corners}, by away team: {self.mean_team_against_corners}\n'
            f'Mean fouls committed by {self.team}: {self.mean_team_fouls}, by away team: {self.mean_team_against_fouls}\n'
            f'Mean yellow cards by {self.team}: {self.mean_team_yellow_cards}, by away team: {self.mean_team_against_yellow_cards}\n'
            f'Mean of diff gols(home gols - away gols) by { self.team }: { self.diff_gols_win } if its a win game')

                 
        self.change_mode()
        self.__init__(self.team, self.specific)
        
        if __name__ == "__main__":
            self.description_against()
    
    def description_against(self):
        print('\n')
        print(
            f'{self.team} at {self.specific} games\n'
            f'Mean odds: Win-> {self.mean_odd_to_win}, Draw-> {self.mean_odd_to_draw}, Lose-> {self.mean_odd_to_lose}\n'
            f'Mean odds: {self.odd_total_gols_less_2_5} < 2.5 total gols > {self.odd_total_gols_more_2_5}\n'
            f'Mean shots by {self.team}: {self.mean_team_shoots}, by home team: {self.mean_team_against_shoot}\n'
            f'Mean target shots by {self.team}: {self.mean_team_shoots_target}, by home team: {self.mean_team_against_shoots_target}\n'
            f'Mean corners by {self.team}: {self.mean_team_corners}, by home team: {self.mean_team_against_corners}\n'
            f'Mean fouls committed by {self.team}: {self.mean_team_fouls}, by home team: {self.mean_team_against_fouls}\n'
            f'Mean yellow cards by {self.team}: {self.mean_team_yellow_cards}, by home team: {self.mean_team_against_yellow_cards}\n'
            f'Mean of diff gols(home gols - away gols) by { self.team }: { self.diff_gols_win } if its a win game')
        
if __name__ == "__main__":   
    ts = TeamStatistic('Getafe', year='last')
    ts.description()
