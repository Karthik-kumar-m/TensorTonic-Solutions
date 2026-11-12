from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    mean=float(np.mean(x))
    median=float(np.median(x))
    values, counts = np.unique(x, return_counts=True)
    mode = float(values[np.argmax(counts)])
    a={"mean":mean,"median":median,"mode":mode}
    return a