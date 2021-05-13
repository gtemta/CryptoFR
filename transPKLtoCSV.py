# -*- coding: utf-8 -*-
"""
Created on Mon May 10 23:08:14 2021

@author: Gilgamesh
"""

import pandas as pd

targetcoin = ["BNB","ETH","SOL","BTC","UNI"]
transcoin = ["USDT"]

targetTrans = []
for target in targetcoin:
    targetTrans.append(target+transcoin[0])


for tT in targetTrans:
    inputfile = "./" + tT + ".pkl"
    data = pd.read_pickle(inputfile)
    outputfile = "./" + tT + ".csv"
    print(outputfile)
    data.to_csv(outputfile)
