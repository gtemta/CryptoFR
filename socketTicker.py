# -*- coding: utf-8 -*-
"""
Created on Wed May 12 00:00:48 2021

@author: Gilgamesh
"""

from binance import ThreadedWebsocketManager
import time
import pandas as pd
counter = 0
data = pd.DataFrame()

def main():

    symbol = 'BNBBTC'
    columns= ["Event_Time","Symbol","Open","High","Low","Close","Volume","quote_volume"]
    

    twm = ThreadedWebsocketManager(api_key=api_key, api_secret=api_secret)
    # start is required to initialise its internal loop
    twm.start()

    def handle_socket_message(msg):
        print(f"message type: {msg['e']}")
        temp_data = pd.DataFrame(parseFormat(msg), columns=columns)
        print(temp_data)
        
        
    def parseFormat(mes):
        Event_Time = time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime(mes['E']/1000))
        Symbol = mes['s']
        Open = mes['o']
        High = mes['h']
        Low = mes['l']
        Close = mes['c']
        Volume = mes['v']
        quote_volume = mes['q']
        return Event_Time,Symbol,Open,High,Low,Close,Volume,quote_volume

    twm.start_kline_socket(callback=handle_socket_message, symbol=symbol)

    # multiple sockets can be started
    twm.start_depth_socket(callback=handle_socket_message, symbol=symbol)

    # or a multiplex socket can be started like this
    # see Binance docs for stream names
    streams = ['BNBBTC@miniTicker', 'BNBBTC@bookTicker']
    twm.start_multiplex_socket(callback=handle_socket_message, streams=streams)


if __name__ == "__main__":
   main()