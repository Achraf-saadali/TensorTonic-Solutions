import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns sample variance and standard deviation as Python floats.
    """


    X  , N = np.asarray(x , dtype = np.float64) , len(x)

    mean = np.mean(X)
    variance = (1/(N-1))*np.sum( (X-mean)**2 )

    std_dev = variance**(1/2)

    return {
        "variance" : variance , 
        "std_dev" : std_dev
    }
    
    