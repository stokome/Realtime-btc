from csv import writer
import pandas as pd
import os

data = pd.read_csv('btc_rtd.csv')
vwap_BIN = sum(data['priceBIN']*data['24hourVolumeBIN'])/sum(data['24hourVolumeBIN'])
vwap_FTX = sum(data['priceFTX']*data['24hourVolumeFTX'])/sum(data['24hourVolumeFTX'])
vwap_COIN = sum(data['priceCOIN']*data['24hourVolumeCOIN'])/sum(data['24hourVolumeCOIN'])

print('Volume Weighted Average Price (VWAP) for Binance: ', vwap_BIN)
print('Volume Weighted Average Price (VWAP) for FTX: ', vwap_FTX)
print('Volume Weighted Average Price (VWAP) for Coinbase: ', vwap_COIN)


if (os.path.exists('vwap.csv') == False) or (os.path.exists('vwap.csv') and len(open("vwap.csv", "r").readlines()) == 0):
    headers = ['Date/Time',
               'VWAP_BIN',
               'VWAP_FTX',
               'VWAP_COIN']
    with open('vwap.csv', 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(headers)
        
data_list = [list(data['Date/Time'])[-1], 
             vwap_BIN,
             vwap_FTX,
             vwap_COIN]

with open('vwap.csv', 'a+', newline='') as write_obj:
    csv_writer = writer(write_obj)
    csv_writer.writerow(data_list)