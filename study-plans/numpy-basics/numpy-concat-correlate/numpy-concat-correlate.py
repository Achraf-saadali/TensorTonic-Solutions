import numpy as np

def compare_correlations(a: list, b: list) -> np.ndarray:
    """
    Returns float64 correlation matrices for a, b, and their combined rows.
    """
    
    a , b = np.asarray(a , dtype = np.float64) , np.asarray(b , dtype =  np.float64)

    
    corr_a =  np.corrcoef(a.T)
    corr_b = np.corrcoef(b.T)
    merged = np.concat([a , b ])
    merged = np.corrcoef(merged.T)
    return np.stack([corr_a , corr_b , merged])

    return 
