import numpy as np

def normalize(data: list) -> np.ndarray:
    """
    Returns a float64 matrix standardized independently by column.
    """
    data = np.asarray(data , dtype = np.float64)
    mean  = np.mean(data , axis = 0 )
    std = np.std(data , axis =  0 )

    return (data - mean) / std 
