import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    # Write code here

    # List ------> array of nyumpy 
    x = np.asarray(x)

    # sample size
    n = x.shape[0]

    # sample mean
    x_bar = np.mean(x)

    # sample standard deviation
    
    s = (np.sum((x - x_bar)*(x - x_bar)) /(n-1) )**(0.5)

    return    (x_bar - mu0) / (s/(n)**(0.5))