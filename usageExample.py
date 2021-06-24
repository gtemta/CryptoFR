# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 23:09:46 2021

@author: Gilgamesh
"""

import Wrapper.Binance as Binance
import time


client = Binance.BinanceClient()

targetTran = "BNBUSDT"
start_time = time.time()
kdata = client.getMinsK_lastNhour(targetTran,3)
print("--- %s seconds ---" % (time.time() - start_time))

