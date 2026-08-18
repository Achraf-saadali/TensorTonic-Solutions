import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    """
    Normalize a 2D matrix along specified axis using specified norm.
    """
    # Write code here

    
    # registry to match the type with normalisation method !!!!
    ord_matching = {
        'l2' : 2 , 
        'l1' : 1 , 
        'max':np.inf 
    }

    # List ----------------> numpy array 

    matrix = np.array(matrix)

    # Only and exactly 2D array 
    if matrix.ndim != 2  or norm_type not in ord_matching.keys() or (axis is not None and axis > 1)  :
        return None 



    '''
    If i were to use np.linalg.norm on a None axis ,
    
    it might result in a non-vector norm computation
    
    (axis is None && matrix.ndim != 1) ==> Matrix norm

     exple : 
     matrix = [[1 2] , [3,4]]  => ||matrix||_2 == (eigen_value(matrix@T.matrix))*(0.5) != sum_sqrt(x_ij*x_ij) 

     Solution : 
         we flatten the matrix to 1D array when norm calculation  
    
    '''


    
    # Computation of the norm  

    norm_array = np.linalg.norm (
        # Flattening in case of a None axis 
        matrix  if axis is not None else matrix.flatten() , 
        axis = axis , 
        # L1 norm or L2 norm or max
        ord = ord_matching[norm_type]
    )

    if axis is not None :
        # expand dimension to broadcast in respect of
        # norm axis computation 
        norm_array = np.expand_dims(
            norm_array , 
            axis = axis 
        )

    

    return np.where( norm_array != 0 , matrix/norm_array , matrix)
    
        
        

    
                                 

        
    


    

    

     
    

    

    
    
    
     
    
    
        
        

    
    
    