from pandas import *


# Loading web-based data
from pandas_datareader import data as web
import yfinance as yf
yf.pdr_override()

# load data on the FTSE

FTSE = web.get_data_yahoo(tickers='^FTSE', start="2010-01-1", end="2020-12-31").reset_index()
FTSE['Name'] = 'FTSE' # name of the index

IndicesA = DataFrame() # the overall dataframe

for db in [FTSE]: # append all the individual indices
	IndicesA = IndicesA.append(db,ignore_index=True)

print(IndicesA)