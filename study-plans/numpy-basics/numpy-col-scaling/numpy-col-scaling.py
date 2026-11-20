import numpy as np

def scale_cols(data: list, weights: list) -> np.ndarray:
    """
    Returns a float64 matrix with each column multiplied by its weight.
    """
    X , w = np.asarray(data,dtype = np.float64) , np.asarray(weights , dtype = np.float64)


    return X*w
