import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('btc_rtd.csv')

delhourvol_BIN = [data['24hourVolumeBIN'][i + 1] - data['24hourVolumeBIN'][i] for i in range(len(data['24hourVolumeBIN']) - 1)]
delhourvol_FTX = [data['24hourVolumeFTX'][i + 1] - data['24hourVolumeFTX'][i] for i in range(len(data['24hourVolumeFTX']) - 1)]
delhourvol_COIN = [data['24hourVolumeCOIN'][i + 1] - data['24hourVolumeCOIN'][i] for i in range(len(data['24hourVolumeCOIN']) - 1)]

time_tickers = [x.split()[1] for x in data['Date/Time']][1:]
plt.figure(figsize = (20, 8))
plt.plot(time_tickers, delhourvol_BIN, color = 'red', label = 'Binance')
plt.plot(time_tickers, delhourvol_FTX, color = 'green', label = 'FTX')
plt.plot(time_tickers, delhourvol_COIN, color = 'blue', label = 'Coinbase')
plt.xticks([time_tickers[i] for i in range(0, len(time_tickers), int(len(time_tickers)/5))])
plt.legend()
plt.title('Hourly Volume Changes of Bitcoin in Binance, FTX and Coinbase Exchanges')
plt.show()