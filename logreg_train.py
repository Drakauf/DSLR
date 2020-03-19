import sys
import numpy as np
import pandas as pd
from LIB.ft_maths import ftScale
import re

import seaborn as sns; sns.set()
import matplotlib.pyplot as plt

np_load_old = np.load
np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)

def graphObj():
    retObj = dict()
    retObj["House"] = []
    retObj["Iteration"] = []
    retObj["Value"] = []
    return(retObj)

#if __name__ == "__main__":
#    if "-g" in sys.argv:
#        print("Yes")
#    if len(sys.argv) == 1:
#        sys.exit("python3 logreg_train.py file")
#    else:
#    #try:
#        learningRate = 0.001
#        retCost = []
#        data = pd.read_csv(sys.argv[1], index_col="Index")
#        data = data.dropna()
#        dataFeatures = np.array(data.iloc[:,5:])
#        dataHouses = np.array(data.iloc[:,0])
#        dataColumns = data.columns[5:]
#        np.apply_along_axis(ftScale, 0, dataFeatures)
#        dataFeatures = np.insert(dataFeatures, 0, 1, axis=1)
#        graphObj = graphObj(); 
#        for house in np.unique(dataHouses):
#            isHouse = np.where(dataHouses == house, 1,0)
#            innerW = np.ones(dataFeatures.shape[1])
#            for i in range(5):
#                matmul= dataFeatures.dot(innerW)
#                eCost = isHouse - (1/(1+np.exp(-matmul))) #sigmoid here
#                cost = np.dot(dataFeatures.T, eCost)
#                innerW += learningRate * cost
#                graphObj["House"].append(house)
#                graphObj["Iteration"].append(i)
#                graphObj["Value"].append(innerW[0])
#            retCost.append((innerW, house))
#        ## For precision
#        predictedHouse = []
#        for i in range(0, len(dataFeatures)):
#            hw = "yes"
#            for weight, house in retCost:
#                w =  dataFeatures[i].dot(weight)
#                if hw == "yes" or w > hw:
#                    hw = w
#                    p = house
#            predictedHouse.append(p)
#        #print(sum(predictedHouse == dataHouses)/ dataHouses.shape[0])
#        #Graph
#        df = pd.DataFrame(graphObj, columns=["House", "Iteration", "Value"])
#        g = sns.lineplot(x="Iteration", y="Value", hue="House", data=df)
#        #plt.show()
#    #except:
#       # sys.exit("File doesn't exist")

if __name__ == "__main__":
    if len(sys.argv) != 1:
        filename = sys.argv[1]
        print(graphique)
        if "-g" in sys.argv:
            print("Graphics")
        else:
            print("No Graphics")
        if "-p" in sys.argv:
            print("Precision")
        else:
            print("No Precision")
        res = [x for x in sys.argv if re.search("-iter=", x)]
        if len(res) > 0:
            print("Iterations:")
            print(res[0][res[0].find("=")+1:])
