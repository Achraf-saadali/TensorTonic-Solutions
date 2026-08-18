import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    n = len(A)

    return sum(A[i][i] for i in range(n))
