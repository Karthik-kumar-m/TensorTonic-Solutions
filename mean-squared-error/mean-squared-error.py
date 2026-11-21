import numpy as np

def mean_squared_error(y_pred: list, y_true: list) -> float:
    """
    Returns the error as a float.
    """
    # Write code here
    Y_pred=np.asarray(y_pred,dtype=float)
    Y_true=np.asarray(y_true,dtype=float)
    return float(np.mean((Y_pred-Y_true)**2))