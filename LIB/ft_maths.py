import numpy as np
import math

def ft_count(data):
    l = len(data)
    try:
        data = data[~np.isnan(data)]
        return(len(data))
    except:
        return(l)

def ft_mean(data):
    ret = 0
    for nb in data:
        if not np.isnan(nb):
            ret += nb
    return(ret/ft_count(data))

def ft_std(data):
    ret = 0
    i = 0
    mean = ft_mean(data)
    for nb in data:
        if not np.isnan(nb):
            ret = ret + (nb - mean) ** 2
            i += 1
    ret = ret/i
    ret = ret ** 0.5
    return(ret)

def ft_min(data):
    count = 1
    for nb in data:
        if not np.isnan(nb):
            if count:
                ret = nb
                count = 0
            if nb < ret:
                ret = nb
    return(ret)

def ft_max(data):
    count = 1
    for nb in data:
        if not np.isnan(nb):
            if count:
                ret = nb
                count = 0
            if nb > ret:
                ret = nb
    return(ret)

def ft_percentile(data, nb):
    data.sort()
    k = (len(data)-1) * (nb/100)
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return data[int(k)]
    d0 = data[int(f)] * (c-k)
    d1 = data[int(c)] * (k-f)
    return d0+d1
