import pandas as pd


from openbb_terminal import api as openbb


from features.helpers import vwap, momomentum_suite, sortino
from config.rbos import STOCKS_TO_USE, PLACEMENTS, START

def build():

    ohlc = [
        openbb.stocks.load(ticker=i, start=pd.to_datetime(START)) for i in STOCKS_TO_USE
        ]
