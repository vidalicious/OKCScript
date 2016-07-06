#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from HttpMD5Util import *
from OkcoinFutureAPI import *
from OkcoinSpotAPI import *
from OKCUtils import *
from math import *
import pandas as pd

#初始化apikey，secretkey,url
apikey = '884cde11-ec65-4af5-86b6-b9ddd7ca7b3c'
secretkey = '3ABA8A337EB23E3EB62838A0906ED2AC'
okcoinRESTURL = 'www.okcoin.cn'   #请求注意：国内账号需要 修改为 www.okcoin.cn

oneTickTime = 60
counter = 0

ema10sCount = 10 / oneTickTime #10秒
ema1Count = 60 / oneTickTime # 1分钟的tick数
ema2Count = 60 * 2 / oneTickTime
ema3Count = 60 * 3 / oneTickTime
ema5Count = 60 * 5 / oneTickTime #5分钟tick
ema10Count = 60 * 10 / oneTickTime
ema15Count = 60 * 15 / oneTickTime
ema20Count = 60 * 20 / oneTickTime
ema30Count = 60 * 30 / oneTickTime
ema45Count = 60 * 45 / oneTickTime
ema60Count = 60 * 60 / oneTickTime
ema90Count = 60 * 90 / oneTickTime

ema10s_K = float(2.0 / (ema10sCount + 1))
ema1_K = float(2.0 / (ema1Count + 1))
ema2_K = float(2.0 / (ema2Count + 1))
ema3_K = float(2.0 / (ema3Count + 1))
ema5_K = float(2.0 / (ema5Count + 1))
ema10_K = float(2.0 / (ema10Count + 1))
ema15_K = float(2.0 / (ema15Count + 1))
ema20_K = float(2.0 / (ema20Count + 1))
ema30_K = float(2.0 / (ema30Count + 1))
ema45_K = float(2.0 / (ema45Count + 1))
ema60_K = float(2.0 / (ema60Count + 1))
ema90_K = float(2.0 / (ema90Count + 1))

mean10s = 0
mean1 = 0
mean2 = 0
mean3 = 0
mean5 = 0
mean10 = 0
mean15 = 0
mean20 = 0
mean30 = 0
mean45 = 0
mean60 = 0
mean90 = 0

# targetList1 = []
# targetList2 = []
targetList5 = []
targetList10 = []
targetList20 = []
targetList30 = []
targetList45 = []
targetList60 = []
targetList90 = []

#现货API
okcoinSpot = OKCoinSpot(okcoinRESTURL, apikey, secretkey)

while True:
    lastPrice = getLastPrice(okcoinSpot, 'ltc_cny')
    print 'counter ', counter, 'last price ', lastPrice

    # targetList1.insert(0, float(lastPrice))
    # if len(targetList1) > 60 * 1 / oneTickTime:
    #     targetList1 = targetList1[:60 * 1 / oneTickTime]
    #
    # targetList2.insert(0, float(lastPrice))
    # if len(targetList2) > 60 * 2 / oneTickTime:
    #     targetList2 = targetList2[:60 * 2 / oneTickTime]

    targetList5.insert(0, float(lastPrice))
    if len(targetList5) > 60 * 5 / oneTickTime:
        targetList5 = targetList5[:60 * 5 / oneTickTime]

    targetList10.insert(0, float(lastPrice))
    if len(targetList10) > 60 * 10 / oneTickTime:
        targetList10 = targetList10[:60 * 10 / oneTickTime]

    targetList20.insert(0, float(lastPrice))
    if len(targetList20) > 60 * 20 / oneTickTime:
        targetList20 = targetList20[:60 * 20 / oneTickTime]

    targetList30.insert(0, float(lastPrice))
    if len(targetList30) > 60 * 30 / oneTickTime:
        targetList30 = targetList30[:60 * 30 / oneTickTime]

    targetList45.insert(0, float(lastPrice))
    if len(targetList45) > 60 * 45 / oneTickTime:
        targetList45 = targetList45[:60 * 45 / oneTickTime]

    targetList60.insert(0, float(lastPrice))
    if len(targetList60) > 60 * 60 / oneTickTime:
        targetList60 = targetList60[:60 * 60 / oneTickTime]

    targetList90.insert(0, float(lastPrice))
    if len(targetList90) > 60 * 90 / oneTickTime:
        targetList90 = targetList90[:60 * 90 / oneTickTime]

    buy1 = getBuy1(okcoinSpot, 'ltc_cny')
    sell1 = getSell1(okcoinSpot, 'ltc_cny')

    # mean10s = updateEMABy(float(lastPrice), ema10s_K, mean10s)
    # mean1 = updateEMABy(float(lastPrice), ema1_K, mean1)
    # mean2 = updateEMABy(float(lastPrice), ema2_K, mean2)
    # mean3 = updateEMABy(float(lastPrice), ema3_K, mean3)
    mean5 = updateEMABy(float(lastPrice), ema5_K, mean5)
    mean10 = updateEMABy(float(lastPrice), ema10_K, mean10)
    mean15 = updateEMABy(float(lastPrice), ema15_K, mean15)
    mean20 = updateEMABy(float(lastPrice), ema20_K, mean20)
    mean30 = updateEMABy(float(lastPrice), ema30_K, mean30)
    mean45 = updateEMABy(float(lastPrice), ema45_K, mean45)
    mean60 = updateEMABy(float(lastPrice), ema60_K, mean60)
    mean90 = updateEMABy(float(lastPrice), ema90_K, mean90)

    # variance1 = getVarianceFromList(targetList1, mean1)
    # sd1 = sqrt(variance1)
    #
    # variance2 = getVarianceFromList(targetList2, mean2)
    # sd2 = sqrt(variance2)

    variance5 = getVarianceFromList(targetList5, mean5)
    sd5 = sqrt(variance5)

    variance10 = getVarianceFromList(targetList10, mean10)
    sd10 = sqrt(variance10)

    variance20 = getVarianceFromList(targetList20, mean20)
    sd20 = sqrt(variance20)

    variance30 = getVarianceFromList(targetList30, mean30)
    sd30 = sqrt(variance30)

    variance45 = getVarianceFromList(targetList45, mean45)
    sd45 = sqrt(variance45)

    variance60 = getVarianceFromList(targetList60, mean60)
    sd60 = sqrt(variance60)

    variance90 = getVarianceFromList(targetList90, mean90)
    sd90 = sqrt(variance90)

    lt = []
    lbuy1 = []
    lsell1 = []
    # l10s = []
    # l1 = []
    # l2 = []
    # l3 = []
    l5 = []
    l10 = []
    l15 = []
    l20 = []
    l30 = []
    l45 = []
    l60 = []
    # lsd1 = []
    # lsd2 = []
    lsd5 = []
    lsd10 = []
    lsd20 = []
    lsd30 = []
    lsd45 = []
    lsd60 = []
    lsd90 = []

    lIndex = []

    lt.append(float(lastPrice))
    lbuy1.append(float(lastPrice))
    lsell1.append(float(lastPrice))
    # l10s.append(mean10s)
    # l1.append(mean1)
    # l2.append(mean2)
    # l3.append(mean3)
    l5.append(mean5)
    l10.append(mean10)
    l15.append(mean15)
    l20.append(mean20)
    l30.append(mean30)
    l45.append(mean45)
    l60.append(mean60)
    # lsd1.append(sd1)
    # lsd2.append(sd2)
    lsd5.append(sd5)
    lsd10.append(sd10)
    lsd20.append(sd20)
    lsd30.append(sd30)
    lsd45.append(sd45)
    lsd60.append(sd60)
    lsd90.append(sd90)

    lIndex.append(counter)

    st = pd.Series(lt, index=lIndex)
    sbuy1 = pd.Series(lbuy1, index=lIndex)
    ssell1 = pd.Series(lsell1, index=lIndex)
    # s10s = pd.Series(l10s, index=lIndex)
    # s1 = pd.Series(l1, index=lIndex)
    # s2 = pd.Series(l2, index=lIndex)
    # s3 = pd.Series(l3, index=lIndex)
    s5 = pd.Series(l5, index=lIndex)
    s10 = pd.Series(l10, index=lIndex)
    s15 = pd.Series(l15, index=lIndex)
    s20 = pd.Series(l20, index=lIndex)
    s30 = pd.Series(l30, index=lIndex)
    s45 = pd.Series(l45, index=lIndex)
    s60 = pd.Series(l60, index=lIndex)
    # ssd1 = pd.Series(lsd1, index=lIndex)
    # ssd2 = pd.Series(lsd2, index=lIndex)
    ssd5 = pd.Series(lsd5, index=lIndex)
    ssd10 = pd.Series(lsd10, index=lIndex)
    ssd20 = pd.Series(lsd20, index=lIndex)
    ssd30 = pd.Series(lsd30, index=lIndex)
    ssd45 = pd.Series(lsd45, index=lIndex)
    ssd60 = pd.Series(lsd60, index=lIndex)
    ssd90 = pd.Series(lsd90, index=lIndex)

    d = {"st" : st,
         "buy1" : sbuy1,
         "sell1" : ssell1,
         # "s10s" : s10s,
         # "s1" : s1,
         # "s2" : s2,
         # "s3" : s3,
         "s5" : s5,
         "s10" : s10,
         "s15" : s15,
         "s20" : s20,
         "s30" : s30,
         "s45" : s45,
         "s60" : s60,
         # "sd1" : ssd1,
         # "sd2" : ssd2,
         "sd5" : ssd5,
         "sd10" : ssd10,
         "sd20" : ssd20,
         "sd30" : ssd30,
         "sd45" : ssd45,
         "sd60" : ssd60,
         "sd90" : ssd90
    }

    df = pd.DataFrame(d)

    if counter == 0:
        hasHead = True
    else:
        hasHead = False
    with open("okcoin ltc sampling.csv", "a+") as f:
        df.to_csv(f, header=hasHead)

    counter += 1
    time.sleep(oneTickTime)
