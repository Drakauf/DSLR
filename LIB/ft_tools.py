import numpy as np

def fillRet(data, retD):
    notNum = []
    for i in range(1, len(data)):
        try:
            column = np.array(data[i][1:], dtype=float)
            column = column[~np.isnan(column)]
            if column.any():
                retD[0].append(data[i][0])
                retD[1].append("count")
                retD[2].append("mean")
                retD[3].append("std")
                retD[4].append("min")
                retD[5].append("25")
                retD[6].append("50")
                retD[7].append("75")
                retD[8].append("max")
            else:
                raise Exception()
        except :
            notNum.append(data[i][0])
    return(notNum)
