import sys
from LIB.ft_parse import readData, retData
from LIB.ft_tools import fillRet, updateObj
from LIB.ft_print import printNotNum, printRet
import numpy as np
import csv
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

def getData(house, marks):
    ret = dict()
    i = 0
    for nb in marks:
        if not np.isnan(nb):
            try:
                ret[house[i]]["total"] += marks[i]
                ret[house[i]]["nb"] += 1
            except:
                ret[house[i]] = dict()
                ret[house[i]]["total"] = marks[i]
                ret[house[i]]["nb"] = 1
        i += 1
    return(ret)

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
    print(getData(d,d2))
    #df = pd.DataFrame(dictt, columns = ['sex', 'survived', 'class'])
    #print(df)
    #sns.catplot(x="sex", y="survived", hue="class", kind="bar", data=df)
    #sns.set(style="darkgrid")
    #plt.show()
