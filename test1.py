#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8

from OkcoinSpotAPI import OKCoinSpot
from OkcoinFutureAPI import OKCoinFuture
from OKCUtils import *
import time
import threading
import numpy as np

apikey = '884cde11-ec65-4af5-86b6-b9ddd7ca7b3c'
secretkey = '3ABA8A337EB23E3EB62838A0906ED2AC'
okcoinRESTURL = 'www.okcoin.cn'
symbol = 'ltc_cny'
okcoinSpot = OKCoinSpot(okcoinRESTURL, apikey, secretkey)

# ================ trigger ========================
def sampler():
    oneTick = 3
    while True:
        try:
            ticker = okcoinSpot.ticker(symbol)
            depth = okcoinSpot.depth(symbol)
            print('last', ticker['ticker']['last'], end='  ')
            print('sell1', ticker['ticker']['sell'], end='  ')
            print('buy1', ticker['ticker']['buy'])
            print('spot ticker', ticker)
            print('depth', depth)



            print('kline 5min')
            arr5min = okcoinSpot.kline(symbol, '1min')[-6:-1]
            aveClose = np.mean(arr5min, axis=0)[-2]  # timestamp, open, high, low, close, vol
            print(aveClose)
            print(arr5min)
            print('finish...\n')
        except Exception:
            dummy = 0
        time.sleep(oneTick)
# ==========================================================

def trader():
    while True:
        dummy = 0
# ===========================================================
sampleThread = threading.Thread(target=sampler)
sampleThread.setDaemon(True)
sampleThread.start()

tradeThread = threading.Thread(target=trader)
tradeThread.setDaemon(True)
tradeThread.start()

while True:
    dummy = 0