import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    X=np.asarray(x,dtype=float)
    Y=np.asarray(y,dtype=float)
    d=sum(abs(X-Y))
    return d