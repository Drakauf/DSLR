import sys
import numpy as np
from collections import Iterable
from LIB.ft_maths import ftCount, ftMean, ftStd, ftMin, ftMax, ftPercentile

def fillRet(data, retD):
    notNum = []
    for i in range(1, len(data)):
        try:
            column = np.array(data[i][1:], dtype=float)
            column = column[~np.isnan(column)]
            if column.any():
                retD[0].append(data[i][0])
                retD[1].append(ftCount(column))
                retD[2].append(ftMean(column))
                retD[3].append(ftStd(column))
                retD[4].append(ftMin(column))
                retD[5].append(ftPercentile(column,25))
                retD[6].append(ftPercentile(column,50))
                retD[7].append(ftPercentile(column,75))
                retD[8].append(ftMax(column))
            else:
                raise Exception()
        except :
            notNum.append(data[i][0])
    return(notNum)

def updateObj(dest, src):
    if not type(dest) is dict or not type(src) is dict:
        sys.exit("updateObj : one of your parameter is not a dict")
    for key in src:
        if isinstance(src[key], Iterable):
            for elem in src[key]:
                try:
                    dest[key].append(elem)
                except:
                    dest[key] = [elem]
        else:
            try:
                dest[key] = [dest[key], src[key]]
            except:
                dest[key] = src[key]
    return(dest)
