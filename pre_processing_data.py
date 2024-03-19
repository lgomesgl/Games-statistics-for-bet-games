import pandas as pd
import numpy as np
from split_data import SplitTheData

class PreProcMatchData(SplitTheData):
    def __init__(self, data):
        self.data = data
        self.macth_data()
        self.df = self.match
        self.pre_proc()
        
    def pre_proc(self):
        df_c = self.df.copy()
        df_c['Total_gols'] = df_c['FTHG'] + df_c['FTAG']
        df_c['Total_gols_half'] = df_c['HTHG'] + df_c['HTAG']
        df_c['Result'] = df_c['FTR']
        self.df_pre_proc = df_c
    
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
        
    

def concatenate_datas(paths):
    data = pd.DataFrame({})
    for path in paths:
        df = pd.read_csv(path, delimiter=',')
        data = pd.concat([df, data], axis=0)
    data = data.reset_index(drop=True)
    
    ppmd = PreProcMatchData(data)
    ppsd = PreProcStatisticData(data)
    ppod = PrecProcOddsData(data)
    df = pd.DataFrame({})
    for data in [ppmd.df_pre_proc, ppsd.df, ppod.df]:
        df = pd.concat([df, data], axis=1)
    return df

