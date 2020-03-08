import numpy as np
from LIB.ft_maths import ft_count, ft_mean, ft_std, ft_min, ft_max, ft_percentile

def fillRet(data, retD):
    notNum = []
    for i in range(1, len(data)):
        try:
            column = np.array(data[i][1:], dtype=float)
            column = column[~np.isnan(column)]
            if column.any():
                retD[0].append(data[i][0])
                retD[1].append(ft_count(column))
                retD[2].append(ft_mean(column))
                retD[3].append(np.mean(column))
                retD[4].append(ft_std(column))
                retD[5].append(np.std(column))
                retD[6].append(ft_min(column))
                retD[7].append(np.min(column))
                retD[8].append(ft_percentile(column,25))
                retD[9].append(np.percentile(column,25))
                retD[10].append(np.percentile(column,50))
                retD[11].append(np.percentile(column,50))
                retD[12].append(np.percentile(column,75))
                retD[13].append(np.percentile(column,75))
                retD[14].append(ft_max(column))
                retD[15].append(np.max(column))
            else:
                raise Exception()
        except :
            notNum.append(data[i][0])
    return(notNum)
