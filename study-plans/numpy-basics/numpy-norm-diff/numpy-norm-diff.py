import numpy as np

def norm_diff(a: list, b: list, lo: float, hi: float) -> np.ndarray:
    """
    Returns a float64 array of absolute normalized differences.
    """
    a = np.asarray(a , dtype = np.float64)
    b = np.asarray(b , dtype = np.float64)
    clipped_a = np.clip(a , lo , hi)
    clipped_b = np.clip(b , lo , hi)

    return np.abs(clipped_a - clipped_b) * (1/(hi-lo))
