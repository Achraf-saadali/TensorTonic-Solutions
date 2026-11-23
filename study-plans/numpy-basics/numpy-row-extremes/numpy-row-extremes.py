import numpy as np

def row_extremes(data: list) -> np.ndarray:
    """
    Returns float64 rows of maxima, maximum indices, minima, and minimum indices.
    """
    data = np.asarray(data ,dtype = np.float64)
    minimum , maximum = np.min(data , axis = 1) , np.max(data , axis = 1)
    argmin , argmax = np.argmin(data , axis = 1) , np.argmax(data , axis = 1 )

    return np.asarray([maximum , argmax , minimum , argmin])


    
