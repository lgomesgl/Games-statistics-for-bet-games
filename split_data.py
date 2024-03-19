class SplitTheData:
    '''
        Separating the data into 3 datasets: Match, Statistics and Odds.
        Site: https://www.football-data.co.uk/
    '''
    def __init__(self, data):
        self.data = data
        
    def macth_data(self):
        '''
            Div: league division, Data: Match Date, Time: Time of the match,
            FHTG: Full time home team goals, FTAG: Full time away team gols, FTR: Full time result,
            HTHG: Half time home team goals, HTAG: Half time away team goals, HTR: Half time result.         
        '''
        self.match = self.data[['Div','Date','Time','HomeTeam','AwayTeam','FTHG','FTAG','FTR','HTHG','HTAG','HTR']]
        
    def statistics_data(self):
        '''
            HS: Home team shots, AS: Away team shots,
            HTS: Home team shots on target, ATS: Away team shots on target,
            HC: Home team corners, AC: Away team corners,
            HF = Home Team Fouls Committed, AF = Away Team Fouls Committed,
            HY = Home Team Yellow Cards, AY = Away Team Yellow Cards,
            HR = Home Team Red Cards, AR = Away Team Red Cards.
        '''
        self.statistics = self.data[['HS','AS','HST','AST','HC','AC','HF','AF',
                                           'HY','AY','HR','AR']]       
    def odds_data(self):
        '''
            B365H: Bet365 home win odds, B365D: Bet365 draw odds, B365A: Bet365 away win odds,
            B365>2.5: Bet365 over 2.5 goals, B365<2.5: Bet365 under 2.5 goals,
            B365AHH: Bet365 Asian handicap home team odds, B365AHA: Bet365 Asian handicap away team odds.
        '''
        self.odds = self.data[['B365H','B365D','B365A','B365>2.5','B365<2.5','B365AHH','B365AHA']]
        
        