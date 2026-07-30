import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    # Write code here



    
    # y_true   reshaped to numpy array 
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    # Number of samples 
    N  = y_true.shape[0]

    # [np.arrange(N) , y_true] couples [0,1,2....,N] x [class0,class1 , ...classN]
    # creates [0,class0] , ..... [N,classN]
    return      -np.mean( np.log(y_pred[np.arange(N) , y_true]))

    
    
    
     


    

    

    