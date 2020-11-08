import pandas as pd
import datetime
import numpy as np
import pandas_datareader.data as web
from pandas import Series, DataFrame
import matplotlib as mpl
import time
import matplotlib.dates as mdates
from matplotlib.dates import drange


start = datetime.datetime(2015,1,1)
end = datetime.datetime(2020,9,3)
# delta = datetime.timedelta(hours = 24)
# dates = drange(start,end,delta)

# dtStart = pd.Timestamp('2015-01-01')
# dtEnd = pd.Timestamp('2020-09-03')



df = web.DataReader('GOLD', 'yahoo', start, end)
# print(df.index)
# df.set_index('Date', drop=True, inplace=True)
# print (df.index)

tyme = df.index.values

print(tyme)


close_px = df['Adj Close']
# print(close_px)

# mavg = close_px.rolling(window=100).mean()
# mavg20=close_px.rolling(window=20).mean()
# df.set_index('Date', inplace =True)

import matplotlib.pyplot as plt
from matplotlib import style
from urllib.parse import urlencode


# # Adjusting the size of matplotlib

# mpl.rc('figure', figsize=(8, 7))
# mpl.__version__

fig, ax = plt.subplots(figsize=(8,7))

ax.set(title="Come on motherfucker!")

# # # Adjusting the style of matplotlib
style.use('ggplot')

ax.plot(close_px)

def myFormatter(x, pos):
    newTime = pd.to_datetime(x)
    return newTime.strftime("%m-%d-%Y")


# ax.get_xaxis().set_major_locator(mdates.YearLocator(, month=1, day=1))
ax.get_xaxis().set_major_formatter(mpl.ticker.FuncFormatter(myFormatter))
# date_format = datetime.DateFormatter('%m, %d, %Y') 
plt.setp(ax.get_xticklabels(), rotation=30, ha="right")



# plt.gca().xaxis.set_major_formatter(date_format)

plt.show()

# # mavg.plot(label='mavg')
# # mavg20.plot(label="mavg20")
# plt.legend()
# plt.show()

# # rets = close_px / close_px.shift(1) - 1
# # rets.plot(label='return')


# plt.show()
