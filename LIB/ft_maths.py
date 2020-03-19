import numpy as np
import math

def ftCount(data):
    l = len(data)
    try:
        data = data[~np.isnan(data)]
        return(len(data))
    except:
        return(l)

def ftMean(data):
    ret = 0
    for nb in data:
        if not np.isnan(nb):
            ret += nb
    return(ret/ftCount(data))

def ftStd(data):
    ret = 0
    i = 0
    mean = ftMean(data)
    for nb in data:
        if not np.isnan(nb):
            ret = ret + (nb - mean) ** 2
            i += 1
    ret = ret/i
    ret = ret ** 0.5
    return(ret)

def ftMin(data):
    count = 1
    for nb in data:
        if not np.isnan(nb):
            if count:
                ret = nb
                count = 0
            if nb < ret:
                ret = nb
    return(ret)

def ftMax(data):
    count = 1
    for nb in data:
        if not np.isnan(nb):
            if count:
                ret = nb
                count = 0
            if nb > ret:
                ret = nb
    return(ret)

def ftPercentile(data, nb):
    data.sort()
    k = (len(data)-1) * (nb/100)
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return data[int(k)]
    d0 = data[int(f)] * (c-k)
    d1 = data[int(c)] * (k-f)
    return d0+d1

def ftScale(data):
    mean = ftMean(data)
    std = ftStd(data)
    for i in range(0, len(data)):
        data[i] = (data[i] - mean) / std
    return(data)
