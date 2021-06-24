# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 22:52:36 2021

@author: Gilgamesh
"""

import pandas as pd
import time
from binance.client import Client
from binance import ThreadedWebsocketManager

class BinanceClient():
    def __init__(self):
        self.__api_key = "XX"
        self.__api_secret = "SS"
        self.__client = Client(self.__api_key,self.__api_secret)
    
    def __parseFormat(self, kline):
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
    
    def __getKlineCol(self):
        columns= ["Start_Time","Open","High","Low","Close","Volume","Stop_time"
        ,"Quote_asset_volume","Number_of_trades","Taker_buy_base_asset_volume","Taker_buy_quote_asset_volume"]
        return columns

    def getMinsK_lastNhour(self, targetset, N=3):
        timeset = str(N)+ " hours ago UTC"
        kdata = self.__client.get_historical_klines(targetset, Client.KLINE_INTERVAL_1MINUTE, timeset)
        df = pd.DataFrame(map(self.__parseFormat,kdata), columns=self.__getKlineCol())
        df = df.set_index(self.__getKlineCol()[0])
        return df
#to add more function for chikuwa use



class BianceSocket():
    def __init__(self):
        self.__api_key = "XX"
        self.__api_secret = "SS"
        self.__twm = ThreadedWebsocketManager(api_key=self.__api_key, api_secret=self.__api_secret)


    def __parseKlineFormat(self,mes):
        Event_Time = time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime(mes['E']/1000))
        Symbol = mes['s']
        Open = mes['k']['o']
        High = mes['k']['h']
        Low = mes['k']['l']
        Close = mes['k']['c']
        Volume = mes['k']['v']
        quote_volume = mes['k']['q']
        tradenum = mes['k']['n']
        print("Symbol: ", Symbol)
        print(Event_Time,"OHCL",Open, High, Low, Close)
        print("Vol QVol trade",Volume,quote_volume,tradenum)
        return Event_Time,Symbol,Open,High,Low,Close,Volume,quote_volume,tradenum

    def __parseTradeFormat(self,mes):
        Event_Time = time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime(mes['E']/1000))
        Symbol = mes['s']
        Price = mes['p']
        Quantity = mes['q']
        print("Symbol: ", Symbol)
        print(Event_Time," P&Q",Price, Quantity)
        return Event_Time,Symbol,Price,Quantity

    def __parseBookFormat(self, mes):
        Symbol = mes['s']
        Best_Bid_Price = mes['b']
        Best_Bid_Quantity = mes['B']
        Best_Ask_Price = mes['a']
        Best_Ask_Quantity = mes['A']
        print("Symbol: ", Symbol)
        print(" Bid P&Q",Best_Bid_Price, Best_Bid_Quantity, "Ask P&Q",Best_Ask_Price, Best_Ask_Quantity)
        return Symbol,Best_Bid_Price,Best_Bid_Quantity,Best_Ask_Price,Best_Ask_Quantity

    def handle_kline_socket_message(self,msg):
        print(f"message type: {msg['e']}")
        self.__parseKlineFormat(msg)

    def handle_trade_socket_message(self,msg):
        print(f"message type: {msg['e']}")
        self.__parseTradeFormat(msg)
    
    def handle_book_socket_message(self,msg):
        self.__parseBookFormat(msg)
    