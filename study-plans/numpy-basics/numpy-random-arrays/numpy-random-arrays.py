import numpy as np

def generate_random_array(shape: list, kind: str, seed: int) -> np.ndarray:
    """
    Returns a seeded 2D float64 random array with the requested shape.
    """
    gn =  np.random.default_rng(seed = seed )

    if kind == "normal":
        return gn.normal( size = tuple(shape)  )
        
    return gn.random( tuple(shape)  )
    
