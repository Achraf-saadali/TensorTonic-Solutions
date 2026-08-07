import numpy as np
import math

def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: list or np.ndarray
    Return: np.ndarray of same shape (dtype=float)
    """
    # Write code here
    

    # List ------> numpy array  

    x = np.array(x , dtype = np.float64)


    # Error Function vectorization

    numpy_erf = np.vectorize(math.erf)
    

    # Formula Definition of GeLU
    def GeLu(z) :
        
        return (0.5)*z*(1+numpy_erf(z*((0.5)**(0.5))))


    return GeLu(x)

 

    


      
    
