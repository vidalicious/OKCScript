#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from HttpMD5Util import *
from OkcoinFutureAPI import *
from OkcoinSpotAPI import *

def getLastPrice(spot, symbol):
    info = spot.ticker(symbol)
    if info is not None:
        ticker = info['ticker']
        if ticker is not None:
            return ticker['last']
    return None

def getBuy1(spot, symbol):
    info = spot.ticker(symbol)
    if info is not None:
        ticker = info['ticker']
        if ticker is not None:
            return ticker['buy']
    return None

def getSell1(spot, symbol):
    info = spot.ticker(symbol)
    if info is not None:
        ticker = info['ticker']
        if ticker is not None:
            return ticker['sell']
    return None


# ====================================================================
def updateEMABy(currentValue, ema_K, lastMean):
    if lastMean != 0:
        mean = currentValue * ema_K + lastMean * (1 - ema_K)
    else:
        mean = currentValue
    return mean

def getVarianceFromList(list, mean):
	total = 0
	if list is not None:
		for i in list:
			total += (i - mean) ** 2
		return total / len(list)
	else:
		return 0