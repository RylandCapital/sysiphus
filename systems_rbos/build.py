import pandas as pd
import numpy as np


from openbb_terminal import api as openbb

from system_features.helpers import vwapdist, rsi, cci, macd, sortino, inside, inside_down, inside_up
from system_targets.helpers import rbos_next_day
from configs.rbos import STOCKS_TO_USE, PLACEMENTS, START

def build():

    #returns DataFrame with ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'] 
    dfs = [
        openbb.stocks.load(ticker=i, start=pd.to_datetime(START)) for i in STOCKS_TO_USE
        ]

    #create features
    [i.insert(len(i.columns), 'vwapW', vwapdist(i, reset='W')) for i in dfs] #distance from weekly vwaps
    [i.insert(len(i.columns), 'vwapM', vwapdist(i, reset='M')) for i in dfs] #distance from weekly vwaps
    [i.insert(len(i.columns), 'Sortino', sortino(i, lookback=21)) for i in dfs] #sortino ratio
    [i.insert(len(i.columns), 'Inside', inside(i).values) for i in dfs] #inside day flag
    [i.insert(len(i.columns), 'InsideUp', inside_up(i).values) for i in dfs] #inside and up day flag
    [i.insert(len(i.columns), 'InsideDown', inside_down(i).values) for i in dfs] #inside and down day flag
    
    for i in np.arange(len(dfs)):
        dfs[i] = dfs[i].join(rsi(dfs[i], lookback=14))
        dfs[i] = dfs[i].join(cci(dfs[i], lookback=14))

    dataset = pd.concat(dfs, axis=1)
    dataset = dataset.join(rbos_next_day(dataset)).dropna()
    dataset.drop(['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'], axis=1, inplace=True)

    return 

        
        


    



    
    
