# -*- coding: utf-8 -*-
"""
Created on Sat May  8 22:08:26 2021

@author: Gilgamesh
"""


import pandas as pd
import time
from binance.client import Client


client = Client('API', 'APIsC')


targetcoin = ["THETA","ADA","BNB","BTC","DOT","ETH","SOL","UNI"]
transcoin = ["USDT"]

targetTrans = []
for target in targetcoin:
    targetTrans.append(target+transcoin[0])


def parseFormat(kline):
    Start_Time = time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime(kline[0]/1000))
    Open = kline[1]
    High = kline[2]
    Low = kline[3]
    Close = kline[4]
    Volume = kline[5]
    Stop_time = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(kline[6]/1000))
    Quote_asset_volume = kline[7]
    Number_of_trades = kline[8]  
    Taker_buy_base_asset_volume = kline[9] 
    Taker_buy_quote_asset_volume = kline[10]
    return Start_Time,Open,High,Low,Close,Volume,Stop_time,Quote_asset_volume,Number_of_trades,Taker_buy_base_asset_volume,Taker_buy_quote_asset_volume

def getMinsK_lasthour(targetset,hours):
    timeset = str(hours)+ " hours ago UTC"
    data = client.get_historical_klines(targetset, Client.KLINE_INTERVAL_1MINUTE, timeset)
    df = pd.DataFrame(map(parseFormat,data), columns=columns)
    return df


columns= ["Start_Time","Open","High","Low","Close","Volume","Stop_time"
        ,"Quote_asset_volume","Number_of_trades","Taker_buy_base_asset_volume","Taker_buy_quote_asset_volume"]

# start_time = ["1 May, 2021"]
# stop_time =  ["2 Jun, 2021"]

# for tT in targetTrans:
#     data = pd.DataFrame()
#     print("Start", tT)
#     counter = 0
#     while counter < len(start_time):
#         alldata = client.get_historical_klines(tT, Client.KLINE_INTERVAL_1MINUTE, start_time[counter],stop_time[counter])
#         print(start_time[counter])
#         temp_data = pd.DataFrame(map(parseFormat,alldata), columns=columns)
#         print("append data size",temp_data.shape[0])
#         data = data.append(temp_data)
#         counter+=1
    
#     data = data.set_index("Start_Time")
#     outputfile = "./" + tT + "5162.csv"
#     data.to_csv(outputfile)
#     print("Finsh & dump ", tT)

start_time = time.time()
targetK = getMinsK_lasthour(targetTrans[0],3)
print("--- %s seconds ---" % (time.time() - start_time))
