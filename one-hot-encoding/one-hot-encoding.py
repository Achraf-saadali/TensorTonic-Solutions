import numpy as np

def one_hot(y, num_classes=None):
    """
    Convert integer labels y ∈ {0,...,K-1} into one-hot matrix of shape (N, K).
    """
    # Write code here

    # List -----------> numpy array 

    y = np.asarray(y)

    # length of the hot encoding
    n = y.shape[0]

    # number of classes
    num_classes = max(y) + 1 if num_classes is None else num_classes

    # Intialise  our return array 
    z = np.zeros((n,num_classes))

    # Set the class of the prediction 
    z[ np.arange(n) , y] = 1

    return z 