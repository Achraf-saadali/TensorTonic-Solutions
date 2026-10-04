import numpy as np

def linear_regression_from_scratch(X: list, y: list, lr: float, epochs: int) -> tuple:
    """
    Returns the fitted weight list and bias.
    """
     
    X_train , y= np.asarray(X) , np.asarray(y)
    N = X_train.shape[0]

    ground_truth = np.asarray(y)

    w  , b = np.zeros(X_train.shape[1]) , 0

    for i in range(epochs):
        y_train = X_train@w + b 

        dw = (2/N) * X_train.T @ (y_train - y)

        db = (2/N) * np.sum(y_train - y)

        w -= lr*dw
        b -= lr*db

    return w , b   
    
    
