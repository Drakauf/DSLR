import sys
from LIB.ft_parse import readData, retData
from LIB.ft_tools import fillRet
from LIB.ft_print import printNotNum, printRet
import numpy as np

if __name__ == "__main__":
    verbose = 0
    lArg = len(sys.argv);
    if lArg == 3 and sys.argv[2] == '-v':
        verbose = 1
    if (lArg != 2 and not verbose):
        sys.exit("Wrong usage: python3 describe.py filename [-v]");
    data = readData(sys.argv[1]);
    retD = retData(["", "Count","Mean","Std","Min","25%","50%","75%","Max"])
    notNum = fillRet(data, retD)
    if verbose:
        printNotNum(notNum)
    printRet(retD)
