import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    # Write code here

    A = np.array(A)
    # Elimination Of :
    # -not Squared 
    # det of A == 0 since A^-1 = (1/det(A))*tranpose(comatrice(A))
    if np.linalg.det(A) == 0 or A.ndim != 2 or A.shape[0] != A.shape[1]:
        return None 

    return np.linalg.inv(A)
