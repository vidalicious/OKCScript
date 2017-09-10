#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8

from OkcoinSpotAPI import OKCoinSpot
from OkcoinFutureAPI import OKCoinFuture
import time
import threading

apikey = '884cde11-ec65-4af5-86b6-b9ddd7ca7b3c'
secretkey = '3ABA8A337EB23E3EB62838A0906ED2AC'
okcoinRESTURL = 'www.okcoin.cn'

okcoinSpot = OKCoinSpot(okcoinRESTURL, apikey, secretkey)

oneTick = 3

flag = False
# ================ trigger ========================
def trigger():
    global flag
    while True:
        flag = True
        time.sleep(oneTick)
# ==========================================================
triggerThread = threading.Thread(target=trigger)
triggerThread.setDaemon(True)
triggerThread.start()

while True:
    # sampling
    if flag:
        flag = False
        print('spot ticker')
        print(okcoinSpot.ticker('ltc_cny'))

    # trading


    # print('spot ticker')
    # print(okcoinSpot.ticker('ltc_cny'))
    #
    # print('spot depth')
    # print(okcoinSpot.depth('ltc_cny'))
    #
    # print('kline 1min')
    # print(okcoinSpot.kline('ltc_cny', '1min')[-5:])
    #
    # print('kline 1min')
    # print(okcoinSpot.kline('ltc_cny', '1min')[-1])
    #
    # time.sleep(1)


print(u' 现货行情 ')
print(okcoinSpot.ticker('ltc_cny'))

print(u' 现货深度 ')
print(okcoinSpot.depth('ltc_cny'))

print (u' 现货历史交易信息 ')
print (okcoinSpot.trades())

print (u' 用户现货账户信息 ')
print (okcoinSpot.userinfo())
#
print (u' 现货历史订单信息查询 ')
print (okcoinSpot.orderHistory('ltc_cny','0','1','2'))




