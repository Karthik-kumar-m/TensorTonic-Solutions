import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    X=np.asarray(x, dtype=float)
    si=1/(1+np.exp(-X))
    return si