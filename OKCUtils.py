#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from HttpMD5Util import *
from OkcoinFutureAPI import *
from OkcoinSpotAPI import *
import pandas as pd

def dataNode(data, index):
    lData = [data]
    lIndex = [index]
    s = pd.Series(lData, index=lIndex)
    return s

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

#///////////////////////////////////////////////////////////
