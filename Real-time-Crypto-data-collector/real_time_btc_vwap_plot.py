import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('vwap.csv')

time_tickers = [x.split()[1] for x in data['Date/Time']]
plt.figure(figsize = (20, 8))
plt.plot(time_tickers, data['VWAP_BIN'], color = 'red', label = 'Binance')
plt.plot(time_tickers, data['VWAP_FTX'], color = 'green', label = 'FTX')
plt.plot(time_tickers, data['VWAP_COIN'], color = 'blue', label = 'Coinbase')
plt.legend()
plt.title('Volume Weighted Average Price (VWAP) Changes of Bitcoin in Binance, FTX and Coinbase Exchanges')
plt.show()