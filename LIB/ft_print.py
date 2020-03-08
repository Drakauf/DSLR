def printNotNum(data):
    if (len(data) != 0):
        print("==> Not numeric features: ", end = "")
        for i in range(0, len(data)-1):
            print("\033[1;31m%s\033[0m" %data[i], end=", ")
        print("\033[1;31m%s\033[0m" %data[i+1], end="")
        print("")

def printRet(data):
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            if (j == 0):
                print("%-15.12s" %data[i][j], end="")
            else:
                print("%18.15s" %data[i][j], end="")
        print("")
