import pandas as pd

from pre_processing_data import concatenate_datas

class TeamStatistic:
    def __init__(self, data, team, specific: str, gols=2.5):
        self.data = data
        self.team = team
        self.specific = specific
        self.modeTeam = 'Home and Away'
        self.change_mode()
        self.filter_by_team()
        self.more_or_less_gols(gols)
        self.mean_odds()
        
    def __str__(self):
        return f'{ self.team } at { self.modeTeam } games'
    
    def change_mode(self):
        if self.specific == 'Home':
            self.modeTeam = 'HomeTeam'
            self.modeLett = 'H'
        if self.specific == 'Away':
            self.modeTeam = 'AwayTeam'
            self.modeLett = 'A'
            
    def filter_by_team(self):
        try:
            self.data_filter = self.data[(self.data[self.modeTeam] == self.team)]
        except:
            self.data_filter = self.data[(self.data['HomeTeam'] == self.team) | (self.data['AwayTeam'] == self.team)]                                                                                                                                                                                                                                                                                        
    
    def more_or_less_gols(self, gols):
        self.gols_team_more = self.data_filter[(self.data_filter[f'FT{ self.modeLett }G']) >= gols]        
        self.gols_team_less = self.data_filter[(self.data_filter[f'FT{ self.modeLett }G']) < gols]
        self.total_more = self.data_filter[(self.data_filter['Total_gols']) >= gols]
        self.total_less = self.data_filter[(self.data_filter['Total_gols']) < gols]
        
    def mean_odds(self):
        self.odd_total_gols_more_2_5 = self.total_more['B365>2.5'].describe().mean()
        self.odd_total_gols_less_2_5 = self.total_less['B365<2.5'].describe().mean()
        
    def description(self):
        print('------------DESCRIPTION--------------')
        print(self.__str__())
        print(f'Mean odds of more then 2.5 gols: { self.odd_total_gols_more_2_5 } at { self.specific } game')
        print(f'Mean odds of less then 2.5 gols: { self.odd_total_gols_less_2_5 } at { self.specific } game')
        if self.specific == 'Home':
            self.specific = 'Away'
        else:
            self.specific = 'Home'
        self.__init__(self.data, self.team, self.specific)
        print(f'Mean odds of more then 2.5 gols: { self.odd_total_gols_more_2_5 } at { self.specific } game')
        print(f'Mean odds of less then 2.5 gols: { self.odd_total_gols_less_2_5 } at { self.specific } game')            
            
ts = TeamStatistic(concatenate_datas(),'Real Madrid', 'Home')

