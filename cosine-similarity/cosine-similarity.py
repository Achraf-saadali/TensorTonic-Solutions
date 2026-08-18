import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    
    #  List -----------------> numpy array 
    a = np.array(a)

    b = np.array(b)
    
    # Compute norm a and check it
    a_norm = np.linalg.norm(a)

    if a_norm == 0 :return 0
        
    # Compute norm b and check it 
    b_norm = np.linalg.norm(b)

    if b_norm == 0 :return 0

    return np.sum(a*b) / (a_norm*b_norm)