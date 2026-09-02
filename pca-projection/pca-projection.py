import numpy as np

def pca_projection(X: list, k: int) -> list:
    """
    Returns the centered data projected onto the top components.
    """
    # Write code here
    
    # Inout features 
    N = len(X)
    # List --------> numpy array 
    X = np.asarray(X , dtype = np.float64)
    
    # Compute the Center 
    mean = np.mean(X,axis = 0 )
    
    # Centerting data 
    X_c =  X - mean 
    
    # Covariance matrix 
    C = (N-1)**(-1)*(X_c.T@X_c)
    
    # Return eigenvalues and eigen vectors 
    eigenvalues , eigenvectors = np.linalg.eig(C)

    

    # First K indices for the biggest eigen values 
    idx_eigen = np.argsort(eigenvalues)[::-1][:k]

    
    
    # Corresponding vectors of the previous eigen values
    W = eigenvectors[:,idx_eigen]

    
      
    # Data projection 
    X_proj = X_c@W
    

    return X_proj
    
    
    

    
    
    
    