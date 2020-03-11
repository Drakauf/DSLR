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

def getData2(house, marks, feature, mean):
    retFormat = dict()    
    retFormat["Feature"] = []
    retFormat["Marks"] = []
    retFormat["House"] = []
    i = 0

    for nb in marks:
        if not np.isnan(nb):
            retFormat["Feature"].append(feature)
            retFormat["Marks"].append(marks[i])
            retFormat["House"].append(house[i])
        i += 1
    return(retFormat)

def getData(house, marks, feature, mean):
    ret = dict()
    i = 0
    j = 0
    retFormat = dict()

    if mean:
        retFormat["Feature"] = [feature]
        retFormat["Marks"] = [0]
        retFormat["House"] = ["Mean"]
    for nb in marks:
        if not np.isnan(nb):
            try:
                ret[house[i]]["total"] += marks[i]
                ret[house[i]]["nb"] += 1
                if mean:
                    retFormat["Marks"][0] += marks[i]
                    j +=1
            except:
                ret[house[i]] = dict()
                ret[house[i]]["total"] = marks[i]
                ret[house[i]]["nb"] = 1
                if mean:
                    retFormat["Marks"][0] += marks[i]
                    j +=1
        i += 1
    if mean:
        retFormat["Marks"][0] = retFormat["Marks"][0] / j
    for elem in ret:
        try:
            retFormat["Feature"].append(feature)
            retFormat["Marks"].append(ret[elem]["total"] / ret[elem]["nb"])
            retFormat["House"].append(elem)
        except:
            retFormat["Feature"] = [feature]
            retFormat["Marks"] = [ret[elem]["total"] / ret[elem]["nb"]]
            retFormat["House"] = [elem]
    return(retFormat)

if __name__ == "__main__":
    lArg = len(sys.argv);
    if (lArg != 2):
        sys.exit("Wrong usage: python3 describe.py filename");

    print("reading data")

    reader = 1
    toRender = dict()
    scale = 0
    mean = 0
    data = readData(sys.argv[1])

    #Loop to determine if we need to scale
    while True:
        try:
            ans = input("Do you want to scale data (y/n):\n")
        except EOFError:
            sys.exit(0)
        except:
            sys.exit(0)
        if ans == "y":
            scale = 1
            break
        elif ans == "n":
            break

    #Loop to determine if we show mean or not in the histogram
    while True:
        try:
            ans = input("Do you want to show mean of each feature  in histogram (y/n):\n")
        except EOFError:
            sys.exit(0)
        except:
            sys.exit(0)
        if ans == "y":
            mean = 1
            break
        elif ans == "n":
            break

    #If scale option is selected
    #if scale:
    #    data2 = np.array(data)
    #    scaler = MinMaxScaler()
    #    scaler.fit(data2[6:,1:])
    #    data3 = scaler.transform(data2[6:,1:])
    #    for i in range(6, len(data)):
    #        colInfo = getData2(data[1][1:], np.array(data3[i-6], dtype=float), data[i][0], mean)
    #        toRender = updateObj(toRender, colInfo)
    #No need to scale
    #else:
    #     for i in range(6, len(data)):
    #        colInfo = getData2(data[1][1:],np.array(data[i][1:], dtype=float), data[i][0], mean)
    #        toRender = updateObj(toRender, colInfo)

    for i in range(1, len(data[1])):
        try:
            toRender["House"].append(data[1][i])
        except:
            toRender["House"] = [data[1][i]]
    print(toRender)
    #df = pd.DataFrame(toRender , columns = ['Feature','Marks','House'])
    #print(data)
    #sns.swarmplot(x="Feature", y="Marks", hue="House", data=df)
    #sns.swarmplot(x="House", y="Marks", hue="Feature", data=df)
    #sns.swarmplot(x="Feature", y="Marks", data=df)
    #sns.set(style="darkgrid")
    #plt.title('scatterPlot')
    #plt.show()
    #print(df)

    #g = sns.PairGrid(df, hue="House")
    #g.map_diag(plt.hist)
    #g.map_offdiag(plt.scatter)
    #g.add_legend();
    #plt.show()
