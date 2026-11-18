import numpy as np

def reshape_array(data: list, operation: str) -> np.ndarray:
    """
    Returns a float64 array with the shape selected by operation.
    """
    data = np.asarray(data ,dtype = np.float64)

    if operation == "flatten":
        return data.flatten()

    if operation == "transpose":
        return np.transpose(data)


    return data[np.newaxis,:]
