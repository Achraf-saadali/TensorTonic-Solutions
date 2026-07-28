import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    # Write code here

    x = np.array(x , dtype = np.float32)

    """
    x is a numpy array  ==>   np.where(condition , do_if_true , otherwise)
                        ==> condition : x >= 0 
                        ==> if_true : x 
                        ==> otherwise : alpha * x
                        """

    """
    f is continuous on IR 
    f is derivable  on IR  <====>  alpha == 1 """
    return np.where(x >= 0 , x , alpha*x)