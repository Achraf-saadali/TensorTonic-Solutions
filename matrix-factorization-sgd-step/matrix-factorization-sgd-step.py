def matrix_factorization_sgd_step(U, V, r, lr, reg):
    """
    Perform one SGD step for matrix factorization.
    """
    # Write code here

    # List -----------------> numpy array
    U = np.array(U , dtype  = np.float64)

    V = np.array(V , dtype = np.float64)
    
    # U of shape (n,) and V of shape (n,) so  we transpose V 
    error = r - U@V.T

    # U_new , V_new
    U_new = U+lr*(error*V - reg*U)
    V_new = V+lr*(error*U - reg*V) 
    
    return (U_new ,V_new )