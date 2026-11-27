import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns mean, median, and mode as Python floats in a dictionary.
    """
    x.sort()
    mode = max(x , key = lambda v : x.count(v))*1.0
    n = len(x)

    mean = sum(x) / n 
    median =  0
    if (n & 1 )== 1 :
        median = (x[n//2])*1.0
    else :
        median = (x[(n-1)//2] + x[n//2])/2

    
    return {
        "mean" : mean ,
        "median" : median , 
        "mode" : mode 
    }
    

    