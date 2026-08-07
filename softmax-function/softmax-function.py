import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here

    #  List --------------> numpy array  

    x = np.array(x , dtype = np.float64)

    
    # Flatten the array  to caculate the maximum 

    maximum = max(x.flatten())

    #  Compute the axis   
    # if 2D array  <===> compute over rows <===> axis = 1 = 2 - 1 = x.ndim - 1
    # if 1D array  <===> compute over columns <===> axis = 0 = 1 - 1 = x.ndim - 1


    axis = x.ndim - 1

    # compute numerator  

    numerator = np.exp(x-maximum)

    # compute denominator over axis 

    denominator = np.sum( np.exp(x-maximum), axis = axis)
    # [[...] , [..] ,[..]] ---> [....]

    #  normalize the denominator 

    denominator = np.expand_dims(denominator , axis = axis )



    return numerator / denominator
    

 

    


    
    

     

    

    

    
    
    
    