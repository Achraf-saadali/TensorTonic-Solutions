import numpy as np

def angle_features(angles: list) -> np.ndarray:
    """
    Returns a (3, n) float64 array with sine, cosine, and tangent rows.
    """
    sinus = np.sin(angles)
    cosinus = np.cos(angles)
    tangente = (sinus/cosinus)

    return np.stack([sinus  , cosinus , tangente])
