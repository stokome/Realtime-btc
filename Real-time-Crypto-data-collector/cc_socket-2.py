import asyncio
import json
import websockets
import datetime
from csv import writer

async def cryptocompare():
    # this is where you paste your api key
    api_key = "dc015ef78098afce470ffe94c0bb505a193943848ba6c4320ff2edf0d652d39b"
    url = "wss://streamer.cryptocompare.com/v2?api_key=" + api_key
    async with websockets.connect(url) as websocket:
        await websocket.send(json.dumps({
            "action": "SubAdd",
            "subs": ["5~CCCAGG~BTC~USD"],
        }))
        flag = 0
        while 1:
            try:
                data = await websocket.recv()
            except websockets.ConnectionClosed:
                break
            try:
                data = json.loads(data)
                print(json.dumps(data, indent=4))
                if 'PRICE' in list(data.keys()) and 'LASTVOLUME' in list(data.keys()):
                    data_list = [data['PRICE'], data['LASTVOLUME'], datetime.datetime.now().strftime("%m/%d/%Y") + " " + datetime.datetime.now().strftime("%H:%M:%S")]
                    if flag == 0:
                        header = ['Price', 'Volume', 'Date']
                        with open('btc_rtd.csv', 'a+', newline='') as write_obj:
                            csv_writer = writer(write_obj)
                            csv_writer.writerow(header)
                    with open('btc_rtd.csv', 'a+', newline='') as write_obj:
                        csv_writer = writer(write_obj)
                        csv_writer.writerow(data_list)
                    flag = 1
            except ValueError:
                print(data)


asyncio.get_event_loop().run_until_complete(cryptocompare())