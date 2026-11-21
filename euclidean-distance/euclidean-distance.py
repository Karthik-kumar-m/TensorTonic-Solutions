import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a Python float.
    """
    X=np.asarray(x,dtype=float)
    Y=np.asarray(y,dtype=float)
    d=X-Y
    res=np.sqrt(np.sum(d**2))
    return res