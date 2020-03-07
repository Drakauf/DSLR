import sys
from LIB.ft_parse import readData, retData

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        sys.exit("Wrong usage: python3 describe.py filename");
    data = readData(sys.argv[1]);
    retD = retData(["", "Count","Mean","Std","Min","25%","50%","75%","Max"])
