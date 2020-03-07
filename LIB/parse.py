import sys
import csv

def readData(str):
    data = []
    try:
        with open(str, 'r') as f:
            fscv = csv.reader(f, delimiter=',')
            try:
                for line in fscv:
                    for i in range(0, len(line)):
                        if fscv.line_num == 1:
                            data.append([]);
                        data[i].append(line[i])
            except csv.Error as err:
                sys.exit("An error occured when reading file: %s" % err)
    except IOError:
        sys.exit("File not accessible")
    return data
