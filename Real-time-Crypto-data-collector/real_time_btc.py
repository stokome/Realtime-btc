from csv import writer
import datetime
import cryptocompare


cryptocompare.cryptocompare._set_api_key_parameter('dc015ef78098afce470ffe94c0bb505a193943848ba6c4320ff2edf0d652d39b')


flag = 0
while 1:
    if flag == 0:
        headers = ['Date/Time', 
                   'Hour', 
                   'Minute', 
                   'priceBIN', 
                   'priceFTX', 
                   'priceCOIN', 
                   'hourVolumeBIN', 
                   'hourVolumeFTX', 
                   'hourVolumeCOIN']
        with open('btc_rtd.csv', 'a+', newline='') as write_obj:
            csv_writer = writer(write_obj)
            csv_writer.writerow(headers)
            flag = 1
    else:
        data_binance = cryptocompare.get_avg('BTC', currency='USD', exchange='binanceusa')
        price_binance = data_binance['PRICE']
        volume_binance = data_binance['VOLUME24HOUR']
        data_ftx = cryptocompare.get_avg('BTC', currency='USD', exchange='ftx')
        price_ftx = data_ftx['PRICE']
        volume_ftx = data_ftx['VOLUME24HOUR']
        data_coin = cryptocompare.get_avg('BTC', currency='USD', exchange='Coinbase')
        price_coin = data_coin['PRICE']
        volume_coin = data_coin['VOLUME24HOUR']
        data_list = [datetime.datetime.now().strftime("%m/%d/%Y") + " " + datetime.datetime.now().strftime("%H:%M"), 
                     datetime.datetime.now().strftime("%H"),
                     datetime.datetime.now().strftime("%M"),
                     price_binance,
                     price_ftx,
                     price_coin,
                     volume_binance,
                     volume_ftx,
                     volume_coin]
        with open('btc_rtd.csv', 'a+', newline='') as write_obj:
            csv_writer = writer(write_obj)
            csv_writer.writerow(data_list)