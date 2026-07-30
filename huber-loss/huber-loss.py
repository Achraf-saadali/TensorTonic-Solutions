import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    # Write code here

    def less_than_T(absolute):
        return 0.5*(absolute**(2))

    def more_than_T(absolute , T ):
        return T*(absolute - 0.5*T)
    

    # Transfrom the label and prediction to numpy arrays 

    y_pred = np.array(y_pred)
    y_true = np.array(y_true)

    # compute the absolute error array 
    abs_error = np.abs(y_pred - y_true)

    # number of trainning 
    N  = len(y_true)

    # loss computation on each slot in the array 
    loss_T = np.where(abs_error <= delta , less_than_T(abs_error) , more_than_T(abs_error,delta))


    # calculate the mean and return it 


    return (N**(-1))*np.sum(loss_T)


    