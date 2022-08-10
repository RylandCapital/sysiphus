import pandas as pd
import pandas_ta as ta
from openbb_terminal import api as openbb

#macd cci rsi
from openbb_terminal.common.technical_analysis import momentum_model

#twitter sentiment is possible 
ticker = 'aapl'
data = openbb.stocks.load(
    ticker=ticker,
    start=pd.to_datetime('01-03-2022'),
)

macd = momentum_model.macd(data["Close"], 12, 26, 9)
rsi = momentum_model.rsi(data["Close"], 100, 100, 1)
cci =  momentum_model.cci(
        data["High"], data["Low"], data["Adj Close"], 14, 0.0015
    )


df_vwap_monthly = ta.vwap(
        high=data["High"],
        low=data["Low"],
        close=data["Close"],
        volume=data["Volume"],
        offset=0,
        anchor='M'
    )

df_vwap_weekly = ta.vwap(
        high=data["High"],
        low=data["Low"],
        close=data["Close"],
        volume=data["Volume"],
        offset=0,
        anchor='W'
    )
