import numpy as np

def pairwise_diff(a: list) -> np.ndarray:
    """
    Returns an (n, n) float64 array of signed pairwise differences.
    """

    a1 , a2 = np.asarray(a , dtype = np.float64) , np.asarray(a ,dtype = np.float64)

    return -a1[np.newaxis ,:] + a2[:,np.newaxis]
