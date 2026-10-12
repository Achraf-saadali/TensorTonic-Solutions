import numpy as np
import pandas as pd
def impute(X: list, method: str = "mean") -> list:
    """
    Returns a new matrix with missing entries filled.
    """
    X = np.asarray(X , dtype = np.float64)

    registry = {
        "mean" : np.nanmean(X,axis = 0 ) , 
        "median" : np.nanmedian(X,axis = 0 )
    }
    method = registry[method]
    for j in range(X.shape[1]):
        X[np.isnan(X[:,j]),j] =  max(0 , method[j])

    return list(X)