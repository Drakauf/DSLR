import re
import sys
import numpy as np
import pandas as pd
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt

from LIB.ft_maths import ftScale

def graphObj():
    retObj = dict()
    retObj["House"] = []
    retObj["Iteration"] = []
    retObj["Value"] = []
    return(retObj)

def logistic(filename, verbose, iterations, lRate, preci, graph, outPut):
    print("\nFile_: \033[1;31m%s\033[0m" %filename)
    data = pd.read_csv(filename, index_col="Index")
    print("File_: \033[1;31mSuccessfully read\033[0m")
    print("\nData_: \033[1;31m%d lines and %d columns\033[0m" %(data.shape[0], data.shape[1])) if verbose else None
    r = data.shape[0]
    data = data.dropna()
    print("Data_: \033[1;31m%d lines dropped because of missing values\033[0m" %(r - data.shape[0])) if verbose else None
    dFeatures = np.array(data.iloc[:,5:])
    dHouses = np.array(data.iloc[:,0])
    dColumns = data.columns[5:]
    np.apply_along_axis(ftScale, 0, dFeatures)
    print("Data_: \033[1;31mScalled, formula: value = (value - mean(a))/std(a); value = a[i] for i in range (len(a))\033[0m") if verbose else None
    print("Iter_: \033[1;31m%d\033[0m" %iterations) if verbose else None
    print("lRate: \033[1;31m%f\033[0m" %lRate) if verbose else None
    
    retCost = []
    gObj = graphObj()
    for house in np.unique(dHouses):
        isHouse = np.where(dHouses == house, 1,0)
        innerW = np.ones(dFeatures.shape[1])
        gObj["House"].append(house)
        gObj["Iteration"].append(0)
        gObj["Value"].append(innerW[0])
        for i in range(iterations):
            matmul= dFeatures.dot(innerW)
            eCost = isHouse - (1/(1+np.exp(-matmul))) #sigmoid here
            cost = np.dot(dFeatures.T, eCost)
            innerW += lRate * cost
            gObj["House"].append(house)
            gObj["Iteration"].append(i + 1)
            gObj["Value"].append(innerW[0])
        retCost.append((innerW, house))

    np.save(outPut, retCost)
    print("\nFile_: \033[1;31mcost saved in %s\033[0m" %outPut)
    
    if preci:
        predictedHouse = []
        for i in range(0, len(dFeatures)):
            hw = "yes"
            for weight, house in retCost:
                w =  dFeatures[i].dot(weight)
                if hw == "yes" or w > hw:
                    hw = w
                    p = house
            predictedHouse.append(p)
        print("\nAccur: \033[1;31m%.10f of accuracy\033[0m" %(sum(predictedHouse == dHouses)/dHouses.shape[0]))
    
    if graph:
       df = pd.DataFrame(gObj, columns=["House", "Iteration", "Value"])
       g = sns.lineplot(x="Iteration", y="Value", hue="House", data=df)
       plt.show()


def helper():
    print("pyhton logreg_train.py file [options*]")
    print("options: \033[1m-g:\033[0m shows graphic")
    print("         \033[1m-p:\033[0m calculate accuracy of the algorithme with applying it to the given dataset")
    print("         \033[1m-v:\033[0m verbose mode, not activated by default, will anyway tell the reading and the output file names")
    print("         \033[1m-iter=Number:\033[0m specify the number of iterations you want by replacing Number, default is \033[31;1m5\033[0m")
    print("         \033[1m-lRate=Number:\033[0m specify the learning rate you want by replacing Number, default is \033[31;1m0.001\033[0m")
    print("         \033[1m-outPut=FileName:\033[0m specify the output filename, default is \033[31;1mretCost\033[0m")
    
if __name__ == "__main__":
    if len(sys.argv) != 1:
        filename = sys.argv[1]
        graphique = (False,True)["-g" in sys.argv]
        precision = (False,True)["-p" in sys.argv]
        verbose = (False,True)["-v" in sys.argv]
        iterations = 5
        res = [x for x in sys.argv if re.search("-iters=", x)]
        if len(res) > 0:
            try:
                iterations = int(res[0][res[0].find("=")+1:])
            except:
                iterations = 5
        lRate = 0.001
        res = [x for x in sys.argv if re.search("-lRate=", x)]
        if len(res) > 0:
            try:
                lRate = float(res[0][res[0].find("=")+1:])
            except:
                lRate = 0.001
        outPut = "retCost"
        res = [x for x in sys.argv if re.search("-outPut=", x)]
        if len(res) > 0:
                outPut = res[0][res[0].find("=")+1:]

        try:        
            logistic(filename, verbose, iterations, lRate, precision, graphique, outPut)
        except:
            print("An error occured")
            helper()
    else:
        helper()
