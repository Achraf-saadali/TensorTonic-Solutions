import numpy as np

def linear_regression_closed_form(X: list, y: list) -> list:
    """
    Returns the optimal weight vector as a list.
    """
    # Write code here


    X , y = np.asarray(X , dtype = np.float64) , np.asarray(y , dtype = np.float64)


    
    W =  np.linalg.inv(X.T@X)@(y.T@X)

    return W