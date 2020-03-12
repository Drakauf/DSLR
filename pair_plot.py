import sys
from LIB.ft_parse import readData, retData
from LIB.ft_tools import fillRet, updateObj
from LIB.ft_print import printNotNum, printRet
import numpy as np
import csv
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

def getData(data, name, table):
    data[name] = []
    for elem in table:
        if not np.isnan(elem):
            data[name].append(elem)
        else:
            data[name].append(np.nan)
    return(data)

if __name__ == "__main__":
    lArg = len(sys.argv);
    if (lArg != 2):
        sys.exit("Wrong usage: python3 describe.py filename");

    print("reading data")

    toRender = dict()
    data = readData(sys.argv[1])

    for i in range(1, len(data[1])):
        try:
            toRender["House"].append(data[1][i])
        except:
            toRender["House"] = [data[1][i]]
    names = ["House"]
    for i in range(6, len(data)):
        toRender = getData(toRender, data[i][0], data[i][1:])
        names.append(data[i][0])
    df = pd.DataFrame(toRender , columns=names)
    print("plotting data, can take  up to a minute")
    g = sns.pairplot(df, hue="House")
    g.map_diag(plt.hist)
    g.map_offdiag(plt.scatter)
    g.add_legend();
    plt.show()
