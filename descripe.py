import sys
from LIB.parse import readData

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        sys.exit("Wrong usage: python3 describe.py filename");
    data = readData(sys.argv[1]);
    print(data)
