import numpy as np

def tile_diff(data: list, reps: int) -> np.ndarray:
    """
    Returns float64 slices of tiled values and next-row differences with a final zero row.
    """
    data = np.asarray(data , dtype = np.float64)

    tiled = np.tile(data , (reps,1))
    diff = np.diff(tiled , axis = 0 , append = tiled[-1:,:] )

    

    return np.concat([[tiled] , [diff]])

    
    
