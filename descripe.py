import sys
from LIB.ft_parse import readData, retData
import numpy as np

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        sys.exit("Wrong usage: python3 describe.py filename");
    data = readData(sys.argv[1]);
    retD = retData(["", "Count","Mean","Std","Min","25%","50%","75%","Max"])
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
    for i in range(0, len(retD)):
        for j in range(0, len(retD[i])):
            if (j == 0):
                print("%-15.12s" %retD[i][j], end="")
            else:
                print("%18.15s" %retD[i][j], end="")

        print("")
