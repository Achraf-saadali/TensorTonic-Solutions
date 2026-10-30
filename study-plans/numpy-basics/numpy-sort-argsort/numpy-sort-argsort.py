import numpy as np

def sort_with_indices(data: list, axis: int) -> np.ndarray:
    """
    Returns a (2, m, n) float64 array of sorted values and source indices.
    """

    arr = np.asarray(data , dtype = np.float64)


    return np.asarray([np.sort(arr , axis = axis) , np.argsort(arr , axis = axis)])
