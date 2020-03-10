import sys
from LIB.ft_parse import readData, retData
from LIB.ft_tools import fillRet, updateObj
from LIB.ft_print import printNotNum, printRet
import numpy as np
import csv
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

def getData(house, marks, feature):
    ret = dict()
    i = 0
    j = 0
    retFormat = dict()
    retFormat["Feature"] = [feature]
    retFormat["Marks"] = [0]
    retFormat["House"] = ["School"]
    for nb in marks:
        if not np.isnan(nb):
            try:
                ret[house[i]]["total"] += marks[i]
                ret[house[i]]["nb"] += 1
                retFormat["Marks"][0] += marks[i]
                j +=1
            except:
                ret[house[i]] = dict()
                ret[house[i]]["total"] = marks[i]
                ret[house[i]]["nb"] = 1
                retFormat["Marks"][0] += marks[i]
                j +=1
        i += 1
    retFormat["Marks"][0] = retFormat["Marks"][0] / j
    for elem in ret:
        try:
            retFormat["Feature"].append(feature)
            retFormat["Marks"].append(ret[elem]["total"] / ret[elem]["nb"])
            retFormat["House"].append(elem)
        except:
            print(marks[0])
            retFormat["Feature"] = [feature]
            retFormat["Marks"] = [ret[elem]["total"] / ret[elem]["nb"]]
            retFormat["House"] = [elem]
    return(retFormat)

if __name__ == "__main__":
    verbose = 0
    lArg = len(sys.argv);
    if lArg == 3 and sys.argv[2] == '-v':
        verbose = 1
    if (lArg != 2 and not verbose):
        sys.exit("Wrong usage: python3 describe.py filename [-v]");
    data = readData(sys.argv[1])
    
    d = ["a", "b", "c", "d", "a"]
    d2 = np.array([1, 3, 5, np.nan, 1.2], dtype=float)

    dictt = {
            'sex':['male','female','female'],
            'survived': [0,1,1],
            'class':['one','two','three'],
            }
    dictt2 = {
            'sex':['male','female','female'],
            'se':['male','female','female'],
            'survived': [3,1,3],
            'class':['o','o','o'],
            'test': 3
            }
    updateObj(dictt, dictt2)
    test = getData(data[1][1:],np.array(data[6][1:], dtype=float), data[6][0])
    test["Feature"].append("Arithman")
    test["Marks"].append(490)
    test["House"].append("School")
    
    test["Feature"].append("Arithman")
    test["Marks"].append(49)
    test["House"].append("Slytherin")

    df = pd.DataFrame(test , columns = ['Feature','Marks','House'])
    sns.catplot(x="Feature", y="Marks", hue="House", kind="bar", data=df)
    sns.set(style="darkgrid")
    plt.title('Histogram')
    plt.show()
    print(df)


