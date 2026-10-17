import numpy as np

def ridge_regression(X: list, y: list, alpha: float, lr: float, epochs: int) -> tuple:
    """
    Returns the fitted weight list and bias.
    """
    X  , y = np.asarray(X) , np.asarray(y)

    w  , b = np.zeros(X.shape[1]) , 0
    N = X.shape[0]

    for _ in range(epochs):
        y_train = X@w + b 
        # Adding regularisation term  
        dw = (2/N)*X.T@(y_train - y) + 2*alpha*w
        db = 2*np.mean(y_train - y)

        w -= lr*dw
        b -= lr*db


    return list(w) , b

        
