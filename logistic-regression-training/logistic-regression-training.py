import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # convert the batch X to numpy array of (n , m)
    # n : number of samples
    # m : number of features 

    X = np.array(X ,dtype = np.float64)
    n  , m   = X.shape 
    # w here is a vector 
    w = np.zeros((m,) , dtype = np.float64)
    # biais 
    b = 0.0

    # Xw + b result in a vector of shape (n,) 
    # So  i dont have to reshape y [ground_truth]
    # convert the y to numpy array  

    y = np.array(y , dtype = np.float64)


    for _ in range(steps):
        # X_train of shape (n,)
        X_train = X@w + b
        y_train = _sigmoid(X_train)

        # variants of w and b according to calculus 
        del_w = np.mean((y_train - y)*X.T)

        del_b = np.mean((y_train - y))

        # And then there is gradient descent
        w -= lr*del_w

        b -= lr*del_b

        
    return (w,b)    

    
        
        

        
    
    

    