import pandas as pd

import numpy as np



data = pd.read_table(r'C:\Users\rmathews\Downloads\ES1HR.txt', delimiter = ",").set_index('Date')
data = data[['Open', 'High', 'Low', 'Close']]

data['is'] = np.where((data['High']<data['High'].shift(1)) & (data['Low']>data['Low'].shift(1)),1,0)
data['os'] = np.where((data['High']>data['High'].shift(1)) & (data['Low']<data['Low'].shift(1)),1,0)

data['gis'] = np.where((data['High']<data['High'].shift(1)) & (data['Low']>data['Low'].shift(1)) & (data['Close']>data['Open'].shift(1)),1,0)
data['ris'] = np.where((data['High']<data['High'].shift(1)) & (data['Low']>data['Low'].shift(1)) & (data['Close']<data['Open'].shift(1)),1,0)



'''inside classifications

structure: inside set-up, or weight given to an indside signal.
has a lot to go with the bars preceding time T which is the close of the 
actual inside bar. t+1 close, the bar after the 

'''
