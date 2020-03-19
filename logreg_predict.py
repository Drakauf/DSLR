import sys
import numpy as np
import pandas as pd
from LIB.ft_maths import ftScale

np_load_old = np.load
np.load = lambda *a, **k: np_load_old(*a, allow_pickle=True, **k)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("python logreg_predict dataFile weightFile")
    data = pd.read_csv(sys.argv[1], index_col = "Index")
    retCost = np.load(sys.argv[2])
    dFeatures = data.iloc[:,5:]
    dFeatures = dFeatures.dropna()
    dFeatures = np.array(dFeatures)
    np.apply_along_axis(ftScale, 0, dFeatures)
    
    retData = dict()
    retData["Hogwarts House"] = []
    for i in range(0, len(dFeatures)):
        hw = "yes"
        for weight, house in retCost:
            w = dFeatures[i].dot(weight)
            if hw == "yes" or w > hw:
                hw = w
                p = house
        retData["Hogwarts House"].append(p)
    df = pd.DataFrame(retData, columns=["Hogwarts House"])
    df.to_csv('houses.csv', index_label="Index")
