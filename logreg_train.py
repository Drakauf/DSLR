import sys
import numpy as np
import pandas as pd

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit("python3 logreg_train.py file")
    try:
        data = pd.read_csv(sys.argv[1], index_col="Index")
        data = data.dropna()
        dataFeatures = np.array(data.iloc[:,5:])
        dataHouses = np.array(data.iloc[:,0])
    except:
        sys.exit("File doesn't exist")
