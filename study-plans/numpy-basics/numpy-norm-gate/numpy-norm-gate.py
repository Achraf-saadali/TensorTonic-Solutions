import numpy as np

def norm_gate(X: list, W: list, threshold: float) -> np.ndarray:
    """
    Returns an (n, k) float64 matrix of norm-gated transformed rows.
    """
    X , w = np.asarray(X , dtype = np.float64) , np.asarray(W , dtype = np.float64)

    Z = X @ w 
    norm = np.linalg.norm(Z , ord = 2 , axis = 1)
     
    res = np.zeros(Z.shape)
    
    res[norm >= threshold,] = Z[norm >= threshold , :]

    return res
