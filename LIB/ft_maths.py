import numpy as np

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
    return(nb/ft_count(data))

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
