import numpy as np

def matrix_inverse(A: list) -> np.ndarray | None:
    """
    Returns the inverse as a NumPy array, or None.
    """
    # Write code here

    def comatrice(A) :

        n  = A.shape[0]

        return np.asarray([[(-1)**(i+j)*
                         np.linalg.det([[A[p][q] for q in range(n) if q !=j]
                                       for p in range(n) if p != i])
                          for j in range(n)]
                          for i in range(n)])
        
    
    A = np.asarray(A , dtype = np.float64)

    if np.linalg.det(A) == 0 or A.ndim != 2 or A.shape[0] != A.shape[1] :
        return None 

    if A.shape[0] == 1 : 
        A[0][0] = 1/A[0][0]
        return A

    elif A.shape[0] == 2 : 
        a , b ,c ,d = A[0][0] , A[0][1] , A[1][0] , A[1][1]

        return np.asarray([[d,-b,],[-c,a]])/(a*d-b*c)
    detA = np.linalg.det(A)


    return (comatrice(A).T)/(detA)
    
    