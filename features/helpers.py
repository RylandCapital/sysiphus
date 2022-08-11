import pandas as pd
import pandas_ta as ta
from openbb_terminal import api as openbb

#macd cci rsi
from openbb_terminal.common.technical_analysis import momentum_model

#sortino
from openbb_terminal.common.quantitative_analysis import qa_model



def vwap(data, reset='W'):
    
    return ta.vwap(
        high=data["High"],
        low=data["Low"],
        close=data["Close"],
        volume=data["Volume"],
        offset=0,
        anchor=reset
    )

def momomentum_suite(data, lookback=14):

    macd = momentum_model.macd(data["Close"], 12, 26, 9)
    rsi = momentum_model.rsi(data["Close"], lookback, 100, 1)
    cci =  momentum_model.cci(
            data["High"], data["Low"], data["Adj Close"], lookback, 0.0015
    )

    return {
        'macd':macd,
        'rsi':rsi,
        'cci':cci
    }

def sortino(data, lookback=21):

    return qa_model.get_sortino(data['Close'].pct_change(), 0, lookback, False)

