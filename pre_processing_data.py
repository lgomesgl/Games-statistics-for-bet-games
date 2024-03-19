import pandas as pd
from split_data import SplitTheData

class PreProcMatchData(SplitTheData):
    def __init__(self, data):
        self.data = data
        self.macth_data()
        self.df = self.match
        self.pre_proc()
        
    def pre_proc(self):
        df = self.df
        df['Total_gols'] = df['FTHG'] + df['FTAG']
        df['Total_gols_half'] = df['HTHG'] + df['HTAG']
        df['Result'] = df['FTR']
        self.df_pre_proc = df
    
class PreProcStatisticData(SplitTheData):
    def __init__(self, data):
        self.data = data
        self.statistics_data()
        self.df = self.statistics
    
class PrecProcOddsData(SplitTheData):
    def __init__(self, data):
        self.data = data
        self.odds_data()
        self.df = self.odds
        
    

def concatenate_datas():
    data = pd.read_csv('D:\LUCAS\Football_2.0\Database\La_liga_23_24.csv', delimiter=',')
    ppmd = PreProcMatchData(data)
    ppsd = PreProcStatisticData(data)
    ppod = PrecProcOddsData(data)
    df = pd.DataFrame({})
    for data in [ppmd.df_pre_proc, ppsd.df, ppod.df]:
        df = pd.concat([df, data], axis=1)
    return df

