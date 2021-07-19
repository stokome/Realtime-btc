import asyncio
import json
import websockets
import datetime
import pandas as pd
                
data_list = []
date_list = []
print('Press Enter to continue and ANY KEY + ENTER to break off')
async def cryptocompare():
    # this is where you paste your api key
    api_key = "dc015ef78098afce470ffe94c0bb505a193943848ba6c4320ff2edf0d652d39b"
    url = "wss://streamer.cryptocompare.com/v2?api_key=" + api_key
    async with websockets.connect(url) as websocket:
        await websocket.send(json.dumps({
            "action": "SubAdd",
            "subs": ["5~CCCAGG~BTC~USD"],
        }))
        while input() == '':
            try:
                data = await websocket.recv()
            except websockets.ConnectionClosed:
                break
            try:
                data = json.loads(data)
                print(json.dumps(data, indent=4))
                if 'PRICE' in list(data.keys()):
                    data_list.append(data)
                    date_list.append(datetime.datetime.now().strftime("%m/%d/%Y") + " " + datetime.datetime.now().strftime("%H:%M:%S"))
            except ValueError:
                print(data)                


asyncio.get_event_loop().run_until_complete(cryptocompare())

data_dict = {}
data_dict['PRICE'] = []
data_dict['DATE'] = []
data_dict['LASTVOLUME'] = []
date_index = 0
for data_element in data_list:
    data_dict['PRICE'].append(data_element['PRICE'])
    data_dict['DATE'].append(date_list[date_index])
    data_dict['LASTVOLUME'].append(data_element['LASTVOLUME'])
    date_index += 1
    
dataframe = pd.DataFrame(data_dict)
dataframe.to_csv('financial_data.csv', index = False)


# LASTVOLUME and file appending in real-time