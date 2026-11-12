import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    var=float(np.var(x,ddof=1))
    sd=float(np.std(x,ddof=1))
    return {"variance":var,"standard_deviation":sd}