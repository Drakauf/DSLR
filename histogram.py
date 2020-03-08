import sys
from LIB.ft_parse import readData, retData
from LIB.ft_tools import fillRet
from LIB.ft_print import printNotNum, printRet
import numpy as np
import csv
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

if __name__ == "__main__":
    verbose = 0
    lArg = len(sys.argv);
    if lArg == 3 and sys.argv[2] == '-v':
        verbose = 1
    if (lArg != 2 and not verbose):
        sys.exit("Wrong usage: python3 describe.py filename [-v]");
    data = readData(sys.argv[1])
    
    dictt = {
            'sex':['male','female','female'],
            'survived': [0,1,1],
            'class':['one','two','three']
            }
    dictt2 = {
            'sex':['male','female','female'],
            'se':['male','female','female'],
            'survived': [3,1,3],
            'class':['o','o','o']
            }
    for key in dictt2:
        print(key)
        for elem in dictt2[key]:
            print(elem)
            try:
                dictt[key].append(elem)
            except:
                dictt[key] = [elem]
    print(dictt)
    df = pd.DataFrame(dictt, columns = ['sex', 'survived', 'class'])
    print(df)
    sns.catplot(x="sex", y="survived", hue="class", kind="bar", data=df)
    sns.set(style="darkgrid")
    plt.show()
