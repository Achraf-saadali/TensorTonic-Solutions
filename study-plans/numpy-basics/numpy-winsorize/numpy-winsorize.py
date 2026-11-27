import numpy as np

def winsorize(data: list, lo_q: float, hi_q: float) -> np.ndarray:
    """
    Returns float64 slices of clipped values, lower mask, and upper mask.
    """

    data = np.asarray(data , dtype = np.float64)
    lower , higher = np.percentile(data , lo_q , axis = 0) , np.percentile(data , hi_q , axis = 0 )
    
    clipped = np.clip(data , lower , higher)

    lower_mask =  (data < clipped).astype(float)

    upper_mask = (data > clipped).astype(float)

    return np.stack([clipped , lower_mask , upper_mask])

    
    

    return clipped
