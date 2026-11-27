import numpy as np

def quantize_and_frame(data: list, decimals: int, pad_width: int) -> np.ndarray:
    """
    Returns float64 slices of rounded, floored, and ceiling-rounded values with zero borders.
    """
    data = np.asarray(data , dtype = np.float64)

    res = [np.round(data , decimals) , np.floor(data) , np.ceil(data)]
    
    stacking = [np.pad(v , pad_width) for v  in res]

    return np.stack(stacking)

    
