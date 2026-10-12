import numpy as np

def logistic_regression(X: list, y: list, lr: float, n_iters: int) -> tuple:
    """
    Returns the fitted weight list and bias.
    """

    # Compute Variales [numpy arrays , length ....]
    X  , y   = np.asarray(X) , np.asarray(y)
    n =  X.shape[0]

    w , b = np.zeros(X.shape[1]) , 0

    for _ in range(n_iters):
        #Collapse the input into a masure of likelihood by pinning it to ]0;1[ 
        y_pred = _sigmoid(X@w + b)

        # Gradient Computation
        dw = (1/n)*X.T@(y_pred - y)
        db = np.mean(y_pred - y)

        #Optimization
        w -= lr*dw
        b -= lr*db
        
    return w , b
def _sigmoid(z):

    return (1 + np.exp(-z))**(-1)