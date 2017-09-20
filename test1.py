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
    counter = 0
    while True:
        try:
            ticker = okcoinSpot.ticker(symbol)
            depth = okcoinSpot.depth(symbol)
            print('last', ticker['ticker']['last'], end='  ')
            print('sell1', depth['asks'][-1], end='  ')
            print('buy1', depth['bids'][0])
            # print('spot ticker', ticker)
            # print('depth', depth)

            kline_1min = okcoinSpot.kline(symbol, '1min')
            MA_5min = np.mean(kline_1min[-6:-1], axis=0)[-2]
            print('MA 5min  ', MA_5min, end='  ')
            MA_10min = np.mean(kline_1min[-11:-1], axis=0)[-2]
            print('MA 10min  ', MA_10min)

            data = {
                'last':dataNode(ticker['ticker']['last'], counter),
                'sell1':dataNode(depth['asks'][-1][0], counter),
                'buy1':dataNode(depth['bids'][0][0], counter),
                'ma5min':dataNode(MA_5min, counter),
                'ma10min':dataNode(MA_10min, counter)
            }

            df = pd.DataFrame(data)

            hasHead = counter == 0
            with open("okcoin ltc sampling20170920.csv", "a+") as f:
                df.to_csv(f, header=hasHead)

            # print('kline 5min')
            # arr5min = okcoinSpot.kline(symbol, '1min')[-6:-1]
            # aveClose = np.mean(arr5min, axis=0)[-2]  # timestamp, open, high, low, close, vol
            # print(aveClose)
            # print(arr5min)
            print('tick end...\n')
            counter += 1
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